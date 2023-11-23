from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches, Pt

from source.DocsFileDataSource import DocsFileDataSource
from source.DocsTextDataSource import DocsTextDataSource


class DocsRepository:

    docsTextDataSource = DocsTextDataSource()
    docsFileDataSource = DocsFileDataSource(Document())

    def createLectureDocs(self, terms, text):

        preparedText = [[section[0], self.docsTextDataSource.textTransformationForDocs(section[1], terms)] for section in text]

        print(preparedText)

        self.docsFileDataSource.makeLectureDocs(text=preparedText, terms=terms)
        self.docsFileDataSource.getDocs()
