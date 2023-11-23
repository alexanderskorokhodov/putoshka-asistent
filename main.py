from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

from domain.repository.LectureRepository import LectureRepository

app = FastAPI()
lectureRepository = LectureRepository()
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