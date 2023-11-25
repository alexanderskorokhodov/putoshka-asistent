form for_api import audio_to_text

class LectureNeuronDataSource:

    def getLectureInfo(self, id):

        src = f"uploaded_docx/{id}.mp3"

        return audio_to_text(src)