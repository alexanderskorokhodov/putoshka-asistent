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


    def createLectureDocs(self, terms, text, lec_id, title, subject):

        preparedText = [[section[0], self.lectureTextDataSource.textTransformationForDocs(section[1], terms)] for section in text]


        self.lectureFileDataSource.makeLectureDocs(text=preparedText, terms=terms, image_path=self.getImageFilePath(lec_id), title=title, subject=subject)


    def getLectureInfo(self, file, title, subject):



        id = self.lectureLocalDataSource.generateId()
        self.lectureLocalDataSource.saveFile(file, f"uploaded_mp3/{id}.mp3")

        data = self.lectureNeuronDataSource.getLectureInfo(id)
        terms = data["terms"]
        text = data["text"]
        shortDescr = data["short_descr"]

        self.createLectureDocs(terms=terms, text=text, lec_id=id, subject=subject, title=title)
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

    def getPdfFile(self, id):
        self.lectureFileDataSource.convertDocxToPdf(id)
        return f"uploaded_docx/{id}.pdf"

    def getCutAudio(self, start, end, id):
        name = f"{id}.mp3"
        self.lectureLocalDataSource.cutAudioFile(start, end, name)
        return f"cut_mp3/{id}.mp3"


