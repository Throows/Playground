import json
from pathlib import Path

jsonPath = Path("resources")
class TextsLang:

    lang = "en_US"
    langJSON = None

    def __init__(self, lang : str):
        langFilePath = jsonPath / (lang + ".json")
        if not langFilePath.exists():
            langFilePath = jsonPath / (self.lang + ".json")
        else:
            self.lang = lang

        with open(langFilePath, "rb") as langFile:
            self.langJSON = json.load(langFile)
        
    def getText(self, key) -> str:
        return self.langJSON[key]

    def printText(self, key : str, *kwargs):
        print(self.langJSON[key].format(*kwargs))