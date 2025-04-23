from langchain_core.vectorstores import InMemoryVectorStore
from core.config import embeddings

vector_store = InMemoryVectorStore(embeddings)

