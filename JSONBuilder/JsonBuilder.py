import ast

# Get the normalized entry type Basic (int, float, str), Array, Object
def getJsonEntryType(strVal : str):
    if len(strVal) == 0:
        simpleType = "None"
    else :
        simpleType = "Basic"
    if strVal.casefold().__contains__("list") or strVal.casefold().__contains__("array"):
        simpleType = "Array"
    elif strVal.casefold().__contains__("dict") or strVal.casefold().__contains__("obj"):
        simpleType = "Dictionnary"
    return simpleType

# Get predicted type of string
def typeOfStrVal(value : str):
    value = value.strip()
    if(len(value) == 0):
        return None
    
    try:
        typeVal = ast.literal_eval(value)
    except ValueError:
        return "String"
    except SyntaxError:
        return "String"
    else:
        if typeVal is set((True, False)):
            return "Boolean"
        if type(typeVal) is int:
            return "Integer"
        elif type(typeVal) is float:
            return "Float"
    return "String"

def convertStrToType(valueType : str, value : str):
    if valueType == "Boolean":
        return bool(value)
    if valueType == "Integer":
        return int(value)
    if valueType == "Float":
        return float(value)
    
    return value
