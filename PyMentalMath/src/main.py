import sys, random
import game

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
    return pow(2, choiceNB - 1)

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
    return 15 if chosenOperation > 15 else chosenOperation

gameSettings = {
    "Difficulty": 1      # TODO
}    

gameStats = {
    "RoundPlayed": 0,
    "score": 0
}

def AskComplementarySettings(): 
    if gameSettings["Mode"] == 1:
        print("Enter the time in seconds : (enter to quit)")
        gameSettings["TimeSec"] = GetChoiceInput(5, 600)
    elif gameSettings["Mode"] == 2:
        print("Enter the number of formula to solve : (enter to quit)")
        gameSettings["Round"] = GetChoiceInput(1, 100)
    elif gameSettings["Mode"] == 4:
        print("Enter the goal of good answer : (enter to quit)")
        gameSettings["Goal"] = GetChoiceInput(1, 100)
    else:
        gameSettings["Indefinite"] = True

def GoalReached() -> bool:
    if gameSettings["Mode"] == 2:
       return gameSettings["Round"] == gameStats["RoundPlayed"]
    if gameSettings["Mode"] == 4:
       return gameSettings["Goal"] == gameStats["score"]
    return False
    #TODO Timer

def Play():
    print("\033c")
    while not GoalReached():
        if game.AskOperation(gameSettings["Operations"], gameSettings["Difficulty"]):
            gameStats["score"] += 1
        gameStats["RoundPlayed"] += 1   

    print("You ended with a score of {} out of {}".format(gameStats["score"], gameStats["RoundPlayed"]))    

def Main() -> None:
    print("Welcome to PyMental Math By Romain Berthoule (v1.0)")
    PrintOperationScreen()
    gameSettings["Operations"] = GetOperationInput()
    PrintModeScreen()
    gameSettings["Mode"] = GetChoiceInput(1, 4)
    AskComplementarySettings()

    while True:
        Play()
        AskQuit()

if __name__ == "__main__":
    random.seed()
    Main()
