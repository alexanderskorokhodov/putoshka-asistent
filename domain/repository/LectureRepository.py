from docx import Document

from data.source.LectureDocxDataSource import LectureDocxDataSource
from data.source.LectureLocalDataSource import LectureLocalDataSource
from data.source.LectureNeuronDataSource import LectureNeuronDataSource
from data.source.LectureTextDataSource import LectureTextDataSource


class LectureRepository:

    lectureTextDataSource = LectureTextDataSource()
    lectureFileDataSource = LectureDocxDataSource(Document())
    lectureLocalDataSource = LectureLocalDataSource()
    lectureNeuronDataSource = LectureNeuronDataSource()


    def createLectureDocs(self, terms, text):

        preparedText = [[section[0], self.lectureTextDataSource.textTransformationForDocs(section[1], terms)] for section in text]

        print(preparedText)

        self.lectureFileDataSource.makeLectureDocs(text=preparedText, terms=terms)


    def getLectureInfo(self, file):

        id = self.lectureLocalDataSource.generateId()
        self.lectureLocalDataSource.saveFile(file, f"uploaded_mp3/{id}.mp3")

        data = self.lectureNeuronDataSource.getLectureInfo(id)
        terms = data["terms"]
        text = data["text"]
        shortDescr = data["short_descr"]

        self.createLectureDocs(terms=terms, text=text)
        self.lectureFileDataSource.saveDocx(id)

        return {
            "short_descr":shortDescr,
            "terms":terms,
            "text":text,
            "id":id
        }

    def saveImage(self, file, id):
        self.lectureLocalDataSource.saveFile(file, f"uploaded_images/{id}.png")

    def getImageFilePath(self, id):
        return f"uploaded_images/{id}.png"

    def getDocxFilePath(self, id):
        return f"uploaded_docx/{id}.docx"

