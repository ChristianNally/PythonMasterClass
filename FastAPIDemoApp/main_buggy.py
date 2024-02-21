import uvicorn
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def index():
    return {"index": "root"}

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

def root():
 print('works')

if __name__ == '__main__':
    uvicorn.run(f"{Path(__file__).stem}:app", host="127.0.0.1", port=8888, reload=True)
