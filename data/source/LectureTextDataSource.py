import pymorphy2


class LectureTextDataSource:
    morph = pymorphy2.MorphAnalyzer()

    def getSimpleWord(self, word):
        splitWord = word.split()
        return ' '.join([self.morph.parse(item)[0].normal_form for item in splitWord])

    def cleanText(self, text):
        symbols = [',', '.', ';', ':']
        for symbol in symbols:
            text = text.replace(symbol, '')
        return text.lower()

    def checkWordIsTerm(self, word, terms):
        preparedTerms = [self.getSimpleWord(self.cleanText(item[0])) for item in terms]
        preparedWord = self.getSimpleWord(self.cleanText(word))

        return preparedWord in preparedTerms

    def textTransformationForDocs(self, text, terms):

        outputText = []
        for item in text.split():
            outputText.append([item + " ", self.checkWordIsTerm(item, terms)])
        return outputText

