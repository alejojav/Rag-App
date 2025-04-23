from langchain.chat_models import init_chat_model
from langchain_cohere import CohereEmbeddings
from langchain.text_splitter import TokenTextSplitter


llm = init_chat_model("command-r-plus", model_provider="cohere")


embeddings = CohereEmbeddings(model="embed-english-light-v3.0")

# para probar el modelo de cohere
#print (llm.invoke("Hello, how are you?"))

# document splitter
splitter = TokenTextSplitter(
    encoding_name="cl100k_base",
    chunk_size=100,
    chunk_overlap=10,
)
