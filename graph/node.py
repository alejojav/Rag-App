#from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

from graph.state import State
from core.vector_store import vector_store
from langchain import hub
from core.config import llm

def retrieve(state: State):
    """
    This function will be used to retrieve the data from the vector store.
    """
    print(state['questions'])
    retrieved_docs = vector_store.similarity_search(state['questions'])
    print(retrieved_docs)
    return {
        "context": retrieved_docs
    }

# create a rag template
prompt = hub.pull("rlm/rag-prompt")

# prompt_template = PromptTemplate.from_template( """
#    You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
#    If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
#    Question: {question} 
#    Context: {context} 
#    Answer:
# """
#)

def generate(state: State):
    """
    This function will be used to generate the data from the vector store.
    """
    docs_content = "\n\n".join([doc.page_content for doc in state['context']])
    message = prompt.invoke({"question": state['questions'], "context": docs_content})
    # message = prompt_template.invoke({"question": state['questions'], "context": docs_content})
    response = llm.invoke(message)
    return {
        "answer": response
    }
    