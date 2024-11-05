import streamlit as st
from transformers import pipeline
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model and create FAISS index only once to save resources
@st.cache_resource
def load_model_and_index():
    # Load sentence transformer for embeddings
    embedder = SentenceTransformer('all-MiniLM-L6-v2')

    # Example documents for retrieval
    documents = [
        "Pipe inspection is essential for maintaining the integrity of industrial systems.",
        "Machine learning can predict failures in pipelines by analysing data trends.",
        "Industry standards for pipe inspection vary depending on the material and usage.",
        "Corrosion detection is a critical step in pipe inspection.",
        "Predictive maintenance uses machine learning to foresee equipment issues before they arise."
    ]

    # Generate document embeddings
    doc_embeddings = embedder.encode(documents)

    # Initialize FAISS index
    d = doc_embeddings.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(doc_embeddings)  # Add embeddings to index

    # Load the language model for generation
    generator = pipeline("text-generation", model="vicgalle/gpt2-alpaca-gpt4")

    return embedder, index, documents, generator

# Load the resources
embedder, index, documents, generator = load_model_and_index()

# Streamlit App Title
st.image("banner.png", use_column_width=True)
st.title("RAG-Based Question Answering System")

# Input Query from the user
query = st.text_input("Enter your query:", "")

# Define a function for the RAG pipeline
def rag_pipeline(query, top_k=2):
    # Embed the query
    query_embedding = embedder.encode([query])
    
    # Retrieve top-k most similar documents
    _, I = index.search(np.array(query_embedding), k=top_k)
    retrieved_docs = [documents[i] for i in I[0]]
    
    # Combine query and retrieved documents
    combined_input = query + " " + " ".join(retrieved_docs)
    
    # Generate a response
    response = generator(combined_input, max_length=150, truncation=True)
    
    return response[0]['generated_text']

# Display the RAG response when a query is entered
if query:
    rag_response = rag_pipeline(query)
    st.write("### RAG Response:")
    st.write(rag_response)
