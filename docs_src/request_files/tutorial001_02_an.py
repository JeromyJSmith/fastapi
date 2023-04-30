from typing import Union

from fastapi import FastAPI, File, UploadFile
from typing_extensions import Annotated

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[Union[bytes, None], File()] = None):
    return {"file_size": len(file)} if file else {"message": "No file sent"}


@app.post("/uploadfile/")
async def create_upload_file(file: Union[UploadFile, None] = None):
    return (
        {"filename": file.filename}
        if file
        else {"message": "No upload file sent"}
    )
