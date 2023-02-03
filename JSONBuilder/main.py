import sys, os
import tomllib
from lang import TextsLang
import JsonBuilder as jBuilder
import json

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

def askFileName():
    textsDatas.printText("question-file-name")
    formatedInput = input().replace(" ", "_")
    if not formatedInput.casefold().__contains__(".json"):
        formatedInput = '.'.join(formatedInput, "json")
    
    # TODO BAD CODE Ugly
    if formatedInput.casefold().__contains__("/"):
        dirs = formatedInput.split("/")
        for dir in dirs:
            if not dir.casefold().__contains__(".json"):
                os.mkdir(savePath + dir)
    return formatedInput

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

# ERROR cant add folder parent to the file
def createNewFile(fileName : str):
    hasEntry  = True
    JSONObject = dict()
    while hasEntry :
        addJsonEntry(JSONObject)
        hasEntry = askOtherEntry()

    with open(fileName, "w") as outfile:
        json.dump(JSONObject, outfile, indent=4)

def main():
    newJsonFile = askNewFile()
    while newJsonFile:
        fileName = askFileName()
        createNewFile(fileName)
        newJsonFile = askNewFile()

# Defining Entry Point
if __name__ == "__main__":
    main()

# TODO Replace questions to ask when new entry by :
# is answer is none then skip