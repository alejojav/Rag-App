from typing import TypedDict
from langchain_core.documents import Document

class State(TypedDict):
    """
       This class will be used to store the state of the application.
    """
    questions: str
    context: list[Document]
    answer: str
