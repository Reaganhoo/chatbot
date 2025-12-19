import os
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
import gradio as gr


# 1. SETUP API KEY
os.environ["GOOGLE_API_KEY"] = "YOUR API"

# 2. LOAD PDF
loader = PyPDFLoader("company_policy.pdf")
documents = loader.load()

print(len(documents))
print(f"{documents[0].page_content[:200]}\n")
print(documents[0].metadata)

# 3. Split text into manageable chunks, overlap so context isn't lost between chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, chunk_overlap=100, add_start_index=True
)
all_splits = text_splitter.split_documents(documents)


print(len(all_splits))

# 4. Create embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

#5. Create vector store
vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

vector_store.add_documents(all_splits)

num_results = 1
retriever = vector_store.as_retriever(search_kwargs={"k": num_results})

#to test similarity search
"""results = vector_store.similarity_search(
    "What time can i eat breakfast?"
)

print(results[0])"""

#6. setup llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.3)

def stream_response(message,history):
    docs = retriever.invoke(message)

    #add all the chunk texts to the knowledge string
    knowledge = ""

    for doc in docs:
        knowledge += doc.page_content+"\n\n"

    # make the call to the llm
    if not knowledge.strip():
        return "I don't know. I couldn't find relevant information in the policy."
        
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use ONLY the provided context to answer the question. "
        "If the answer is not in the context, say you don't know. "
        "Use a maximum of three sentences and keep the answer concise."
    )

    human_prompt = f"""
    Question:
    {message}

    Context:
    {knowledge}
    """

    response = llm.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": human_prompt}
    ])

    return response.content

chatbot = gr.ChatInterface(
    stream_response,
    title="REAGAN HOTEL CHATBOT",
    textbox = gr.Textbox(placeholder="Ask me anything about the company policy",container = False,autoscroll = True, scale = 7)
)

chatbot.launch()

        








