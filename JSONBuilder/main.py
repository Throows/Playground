import sys, os
import tomllib
import JsonBuilder as jBuilder
import json
import datetime
from pathlib import Path
from lang import TextsLang

def boolFromInput(inputData : str, yesForLang : str):
    return (inputData.casefold().__contains__(yesForLang) and inputData.casefold() != "")

with open("config.ini", "rb") as conf:
    config = tomllib.load(conf)

print("Python Version : " + sys.version)
print("Software Version : " + config["version"])

textsDatas = TextsLang(config["LANG"]["language"])
savePath = config["SETTINGS"]["savePath"]
print("------ " + textsDatas.getText("name") + " ------")

def askEntryType() -> str:
    textsDatas.printText("question-entry-type")
    typeStr = input()
    return jBuilder.getJsonEntryType(typeStr)

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
    filePath = savePath / filePath
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
    typeJson = jBuilder.typeOfStrVal(valueStr)
    return jBuilder.convertStrToType(typeJson, valueStr)

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
        newValue = True
        while newValue:
            value = askEntryValue()
            if value != None:
                arrayVal.append(value)
            else:
                newValue = False
        obj[EName] = arrayVal
    elif EType == "Dictionnary":
        hasEntry  = True
        newDict = dict()
        while hasEntry :
            hasEntry = addJsonEntry(newDict)
        obj[EName] = newDict
    elif EType == "Basic":
        EValue = askEntryValue()
        obj[EName] = EValue
    return True

def createNewFile(filePath : Path):
    hasEntry  = True
    JSONObject = dict()
    while hasEntry :
        hasEntry = addJsonEntry(JSONObject)

    with open(filePath.absolute(), "w") as outfile:
        json.dump(JSONObject, outfile, indent=4)
    
    textsDatas.printText("json-file-created", str(filePath))

def main():
    newJsonFile = askNewFile()
    while newJsonFile:
        filePath = askFilePath()
        createNewFile(filePath)
        newJsonFile = askNewFile()

# Defining Entry Point
if __name__ == "__main__":
    main()