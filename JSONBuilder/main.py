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

def askEntryType():
    textsDatas.printText("question-entry-type")
    typeStr = input()
    return jBuilder.getJsonEntryType(typeStr)

def askEntryName():
    textsDatas.printText("question-entry-name")
    return input().replace(" ", "-")

def askNewFile():
    textsDatas.printText("question-new-file")
    return boolFromInput(input(), textsDatas.getText("yes"))

def askFilePath() -> Path:
    textsDatas.printText("question-file-name")
    rawFilePath = input()

    filePath = Path(rawFilePath)
    filePath = savePath / filePath
    if not filePath.exists():
        filePath.mkdir(parents= True)

    if filePath.is_dir():
        dateNow = datetime.datetime.now()
        filePath = filePath / dateNow.strftime("Save_%m_%d_%Y-%H:%M.json")
    return filePath

def askEntryValue():
    textsDatas.printText("question-entry-value")
    valueStr = input()
    typeJson = jBuilder.typeOfStrVal(valueStr)
    return jBuilder.convertStrToType(typeJson, valueStr)

def askOtherArrayValue():
    textsDatas.printText("question-add-array-value")
    return boolFromInput(input(), textsDatas.getText("yes"))

def askOtherEntry():
    textsDatas.printText("question-add-entry")
    return boolFromInput(input(), textsDatas.getText("yes"))

def addJsonEntry(obj : dict):
    EType = askEntryType()
    EName = askEntryName()
    if EType == "Array":
        arrayVal = list()
        newValue = True
        while newValue:
            arrayVal.append(askEntryValue())
            newValue = askOtherArrayValue()
        obj[EName] = arrayVal
    elif EType == "Dictionnary":
        hasEntry  = True
        newDict = dict()
        while hasEntry :
            addJsonEntry(newDict)
            hasEntry = askOtherEntry()
        obj[EName] = newDict
    else:
        EValue = askEntryValue()
        obj[EName] = EValue

def createNewFile(filePath : Path):
    hasEntry  = True
    JSONObject = dict()
    while hasEntry :
        addJsonEntry(JSONObject)
        hasEntry = askOtherEntry()

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

# TODO Replace questions to ask when new entry by :
# is answer is none then skip