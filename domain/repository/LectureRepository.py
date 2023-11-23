from docx import Document

from data.source.LectureDocxDataSource import LectureDocxDataSource
from data.source.LectureLocalDataSource import LectureLocalDataSource
from data.source.LectureTextDataSource import LectureTextDataSource


class LectureRepository:

    lectureTextDataSource = LectureTextDataSource()
    lectureFileDataSource = LectureDocxDataSource(Document())
    lectureLocalDataSource = LectureLocalDataSource()


    def createLectureDocs(self, terms, text):

        preparedText = [[section[0], self.lectureTextDataSource.textTransformationForDocs(section[1], terms)] for section in text]

        print(preparedText)

        self.lectureFileDataSource.makeLectureDocs(text=preparedText, terms=terms)
        self.lectureFileDataSource.getDocs()


    def saveAudioFile(self, file):
        id = self.lectureLocalDataSource.generateId()
        self.lectureLocalDataSource.saveFile(file, f"uploaded_mp3/{id}.mp3")
        return id

    def saveImage(self, file, id):
        self.lectureLocalDataSource.saveFile(file, f"uploaded_images/{id}.png")

    def getImageFilePath(self, id):
        return f"uploaded_images/{id}.png"

    def getDocxFilePath(self, id):
        return f"uploaded_images/{id}.docx"

