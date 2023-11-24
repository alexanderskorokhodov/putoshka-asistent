import uuid
from pydub import AudioSegment
import sys
import os

class LectureLocalDataSource:
    def saveFile(self, file, name):
        with open(name, "wb") as mp3_file:
            mp3_file.write(file)
    def generateId(self):
        unique_id = uuid.uuid4()
        return str(unique_id)

    def cutAudioFile(self, start, end, name):
        song = AudioSegment.from_mp3(name)
        cutting = song[-(end * 1000):start * 1000]

        cutting.export(f"cut_mp3/{name}", format="mp3")

