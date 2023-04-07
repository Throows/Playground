import sys 

# --- Game displays ---
def PrintOperationScreen():
    print("\033c")
    print("Operations : ")
    print("\t1 - Additions")
    print("\t2 - Soustractions")
    print("\t3 - Multiplicatons")
    print("\t4 - Divisions")
    print("\t5 - All operations")
    
    print("Enter the numbers of your choice (sepatate by \",\") : (enter to quit)")

def PrintModeScreen():
    print("\033c")
    print("Game Modes : ")
    print("\t1 - Timer")
    print("\t2 - Number of Operation")
    print("\t3 - Indefinite")
    print("\t4 - Goal")
    print("Enter the number of your choice : (enter to quit)")

def AskQuit():
    print("Do you want to exit ? (any keys: yes, n: no)")
    userInput = input(">>> ")
    if "n" in userInput:
        return
    print("GoodBye !")
    exit()

def OperationToChoice(choiceNB: int) -> int:
    return pow(2, choiceNB)

def GetChoiceInput(minChoice: int, maxChoice: int, choice = None) -> int:
    userInput = input(">>> ") if choice is None else choice
    if userInput == "":
        AskQuit()
        return GetChoiceInput(minChoice, maxChoice)
    try:
        userInput = int(userInput)
        if userInput > maxChoice or userInput < minChoice:
            raise Exception("Error : Out of bounds ({} - {})".format(minChoice, maxChoice))
        return userInput
    except ValueError:
        print("Error : Not an Integer")
    except Exception as e:
        print(e)

    return GetChoiceInput(minChoice, maxChoice)

def GetOperationInput() -> int:
    userInput = input(">>> ")
    if userInput == "":
        AskQuit()
        return GetOperationInput()
    chosenOperation = 0
    if "," in userInput :
        args = userInput.split(",")
        isValid = True
        for arg in args:
            try: 
                operation = int(arg)
                chosenOperation += OperationToChoice(operation)
            except ValueError:
                isValid = False
                break  
        
        if not isValid: 
            chosenOperation = GetOperationInput() 
    elif GetChoiceInput(1, 5, userInput):
        chosenOperation = OperationToChoice(int(userInput))
    else:
        chosenOperation = GetOperationInput()
    return 30 if chosenOperation > 30 else chosenOperation

gameInfos = {}    

def AskComplementarySettings(): 
    if gameInfos["Mode"] == 1:
        print("Enter the time in seconds : (enter to quit)")
        gameInfos["TimeSec"] = GetChoiceInput(5, 600)
    elif gameInfos["Mode"] == 2:
        print("Enter the number of formula to solve : (enter to quit)")
        gameInfos["Round"] = GetChoiceInput(1, 100)
    elif gameInfos["Mode"] == 4:
        print("Enter the goal of good answer : (enter to quit)")
        gameInfos["Goal"] = GetChoiceInput(1, 100)
    else:
        gameInfos["Indefinite"] = True

def Play():
    print("\033c")
    print(gameInfos)

def Main() -> None:
    print("Welcome to PyMental Math By Romain Berthoule (v1.0)")
    PrintOperationScreen()
    gameInfos["Operations"] = GetOperationInput()
    PrintModeScreen()
    gameInfos["Mode"] = GetChoiceInput(1, 4)
    AskComplementarySettings()

    while True:
        Play()
        AskQuit()

if __name__ == "__main__":
    Main()
