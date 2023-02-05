import sys, tomllib, JsonBuilder, json, datetime, lang
from pathlib import Path

with open("config.ini", "rb") as conf:
    config = tomllib.load(conf)

textsDatas = lang.TextsLang(config["LANG"]["language"])

def boolFromInput(inputData : str, yesForLang : str) -> bool:
    return (inputData.casefold().__contains__(yesForLang) and inputData.casefold() != "")

def askEntryType() -> str:
    textsDatas.printText("question-entry-type")
    typeStr = input()
    return JsonBuilder.getJsonEntryType(typeStr)

def askEntryName() -> str:
    textsDatas.printText("question-entry-name")
    return input().replace(" ", "-")

def askNewFile() -> bool:
    textsDatas.printText("question-new-file")
    return boolFromInput(input(), textsDatas.getText("yes"))

def askFilePath() -> Path:
    textsDatas.printText("question-file-name")
    rawFilePath = input()

    filePath = Path(rawFilePath)
    filePath = config["SETTINGS"]["savePath"] / filePath
    if not filePath.is_file() and len(filePath.suffix) == 0:
        dateNow = datetime.datetime.now()
        filePath = filePath / dateNow.strftime("Save_%m_%d_%Y-%H:%M.json")
    
    filePath.parents[0].mkdir(parents=True, exist_ok=True)
    return filePath

def askEntryValue():
    textsDatas.printText("question-entry-value")
    valueStr = input()
    if len(valueStr) == 0:
        return None
    typeJson = JsonBuilder.typeOfStrVal(valueStr)
    return JsonBuilder.convertStrToType(typeJson, valueStr)

def askBoolAnswer(question : str) -> bool:
    textsDatas.printText(question)
    return boolFromInput(input(), textsDatas.getText("yes"))

def addJsonEntry(obj : dict) -> bool:
    EType = askEntryType()
    if EType == "None":
        return False
    EName = askEntryName()
    if EType == "Array":
        arrayVal = list()
        value = askEntryValue()
        while value != None:
            arrayVal.append(value)
            value = askEntryValue()
        obj[EName] = arrayVal
    elif EType == "Dictionnary":
        newDict = dict()
        while addJsonEntry(newDict) :
            continue
        obj[EName] = newDict
    elif EType == "Basic":
        EValue = askEntryValue()
        obj[EName] = EValue
    return True

def createNewFile(filePath : Path):
    JSONObject = dict()
    while addJsonEntry(JSONObject):
        continue
    with open(filePath.absolute(), "w") as outfile:
        json.dump(JSONObject, outfile, indent=4)
    
    textsDatas.printText("json-file-created", str(filePath))

print("Python Version : " + sys.version)
print("Software Version : " + config["version"])
print("------ " + textsDatas.getText("name") + " ------")
while askNewFile():
    filePath = askFilePath()
    createNewFile(filePath)