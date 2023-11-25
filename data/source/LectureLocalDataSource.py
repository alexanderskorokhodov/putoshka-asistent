import uuid
from pydub import AudioSegment
import os

class LectureLocalDataSource:
    def saveFile(self, file, name):
        with open(name, "wb") as mp3_file:
            mp3_file.write(file)
    def generateId(self):
        unique_id = uuid.uuid4()
        return str(unique_id)

    def cutAudioFile(self, start, end, name):
        current_directory = os.getcwd()
        print(current_directory + " ###########")
        song = AudioSegment.from_mp3(f"{current_directory}/uploaded_mp3/{name}")
        ten_seconds = 10 * 5000

        first_10_seconds = song[int(start)*10:int(end)*10]

        first_10_seconds.export(f"{current_directory}/cut_mp3/{name}", format="mp3")


