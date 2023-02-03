import json
import os

langFileFormat = "resources/{}.json"

class TextsLang:

    lang = "en_US"
    langJSON = None

    def __init__(self, lang):
        if os.path.exists(langFileFormat.format(lang)):
            langFilePath = langFileFormat.format(lang)
            self.lang = lang
        else:
            langFilePath = langFileFormat.format(self.lang)

        with open(langFilePath, "rb") as langFile:
            self.langJSON = json.load(langFile)
        
    def getText(self, key):
        return self.langJSON[key]

    def printText(self, key : str, *kwargs):
        print(self.langJSON[key].format(*kwargs))