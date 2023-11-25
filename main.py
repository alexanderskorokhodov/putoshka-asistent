from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import urllib3
from domain.repository.LectureRepository import LectureRepository
from fastapi.middleware.cors import CORSMiddleware
from docx2pdf import convert
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
lectureRepository = LectureRepository()

urllib3.disable_warnings()
origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

app.mount("/uploaded_images", StaticFiles(directory="uploaded_images"), name='uploaded_images')
@app.post("/upload_lecture")
async def uploadLecture(title:str, subject:str, file: UploadFile):
    contents = await file.read()

    data = lectureRepository.getLectureInfo(contents, title, subject)
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
    img_path = lectureRepository.getDocxFilePath(id)
    return FileResponse(img_path, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename=f"{id}.docx")

@app.get("/get_pdf")
async def getPdf(id: str):
    img_path = lectureRepository.getPdfFile(id)
    return FileResponse(img_path, filename=f"{id}.pdf")

@app.get("/get_voice_term")
async def getPdf(start: str, end: str, id: str):
    img_path = lectureRepository.getCutAudio(start, end, id)
    return FileResponse(img_path, filename=f"{id}.mp3")

