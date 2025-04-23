
from langchain.document_loaders import PyPDFLoader

def load_pdf_pages(file_path: str):
    """
    this function is used to load pdf pages
    it will be called when the user uploads a pdf file
    """
    pages = [] # list to store the pages (documents)
    loader = PyPDFLoader(file_path)
    for page in loader.load(): # load() -> return Object type Document (page_content, metadata)
        pages.append(page.page_content) #-> add page_content to the list (str) (no boject Document)
    return pages