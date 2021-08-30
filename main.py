# An API to upload files to a server
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/")
async def root(file: UploadFile = File(...)):
    return {"file_name": file.filename}