import tempfile
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel



from utils import load_pdf_pages


from core.config import llm, embeddings, splitter
from core.vector_store import vector_store
from graph.main_graph import graph

app = FastAPI(
    title="Document Indexing and Search API",
    description="API for indexing and searching documents using Langchain and Cohere",
    version="1.0.0", 
    contact={
        "name": "Your Name",
        "email": "youremail@email.com"}
)

@app.post(
        "/index-data",
        tags=["Indexing"], # this will be used to group the endpoints in the swagger UI
        summary="Index data from a document",
)
async def index_data(file: UploadFile = File(...)):
    """
    this function is used to index data from a document
    it will be called when the user uploads a document
    the funtion will do the following:
    1. load document
    2. document splitting
    3. indexing
    """

# save the file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(await file.read())
        temp_path = temp_file.name

        try:
            # 1. load document
            list_of_pages = load_pdf_pages(temp_path)

            # print(list_of_pages)
            # print(type(list_of_pages))

            # 2. document splitting
            fragments = splitter.create_documents(list_of_pages)
            
            # print(len(fragments))

            # 3. indexing
            vector_store.add_documents(documents=fragments)

            return JSONResponse(
                status_code=200, 
                content={
                    "message": "Document indexed successfully",
                }
            )
        except Exception as e:
            return JSONResponse(
                status_code=500, 
                content={
                    "error": str(e),
                }
            )
        finally:
            # clean up the temporary file
            temp_file.close()
            os.remove(temp_path)
                

#    if file.content_type == "application/pdf":
#        return "PDF file uploaded successfully"
#    else:
#        return "File type not supported"

# schema for the request data
class RequestData(BaseModel):
    """
    this class is used to store the data for the request
    """
    prompt: str


@app.post(
        "/search-data",
        tags=["Search"], 
        summary="Search data from the document",
    )
async def search_data(request: RequestData):
    """
    this function is used to search data from the document
    """
    
    # query
    prompt = request.prompt 

    # grafo
    response = graph.invoke({"questions": prompt}) 

    #return response["answer"]

    content = response["answer"].content

    return JSONResponse(
        status_code = 200,
        content = {
            "answer": content
         }
     ) # return the answer from the graph
