import uuid

class LectureLocalDataSource:
    def saveFile(self, file, name):
        with open(name, "wb") as mp3_file:
            mp3_file.write(file)
    def generateId(self):
        unique_id = uuid.uuid4()
        return str(unique_id)
