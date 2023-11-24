from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import urllib3
from domain.repository.LectureRepository import LectureRepository
from fastapi.middleware.cors import CORSMiddleware
from docx2pdf import convert

app = FastAPI()
lectureRepository = LectureRepository()

urllib3.disable_warnings()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])


@app.post("/upload_lecture")
async def uploadLecture(file: UploadFile):
    contents = await file.read()
    data = lectureRepository.getLectureInfo(contents)
    return data

@app.post("/upload_image")
async def uploadImage(id: str, file:UploadFile):
    contents = await file.read()
    lectureRepository.saveImage(contents, id)

@app.get("/get_image")
async def getImage(id: str):
    img_path = lectureRepository.getImageFilePath(id)
    return FileResponse(img_path, media_type="image/png", filename=f"{id}.png")

@app.get("/get_docx")
async def getDocx(id: str):
    img_path = lectureRepository.getImageFilePath(id)
    return FileResponse(img_path, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename=f"{id}.mp3")