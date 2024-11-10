import random

def AskOperation(mode: int, difficulty: int) -> bool:
    availableOperation = []
    for i in range(4):
        if (mode >> i) & 1:
            availableOperation.append(i)

    toAsk = random.randint(0, len(availableOperation) - 1) 

    if availableOperation[toAsk] == 0:
        return AskSum(10)
    if availableOperation[toAsk] == 1:
        return AskSubstraction(10)
    if availableOperation[toAsk] == 2:
        return AskMultiplication(10)
    if availableOperation[toAsk] == 3: 
        return AskDivision(10)
    return False

def AskSum(max: int, minInt: int = 1) -> bool:
    a = random.randint(minInt, max)
    b = random.randint(minInt, max)

    print("What is the answer for {} + {}".format(a, b))
    answer = input(">>> ")
    try:
        answer = int(answer)
        if answer == (a+b):
            print("Good !")
            return True   
        else:
            print("Wrong, the answer was {}".format(a+b))  
            return False
    except ValueError:
        print("Error: Not an integer")
        return False
    
def AskSubstraction(max: int, minInt: int = 1) -> bool:
    a = random.randint(minInt, max)
    b = random.randint(minInt, max)

    print("What is the answer for {} - {}".format(a, b))
    answer = input(">>> ")
    try:
        answer = int(answer)
        if answer == (a-b):
            print("Good !")
            return True   
        else:
            print("Wrong, the answer was {}".format(a-b))  
            return False
    except ValueError:
        print("Error: Not an integer")
        return False

def AskMultiplication(max: int, minInt: int = 1) -> bool:
    a = random.randint(minInt, max)
    b = random.randint(minInt, max)

    print("What is the answer for {} * {}".format(a, b))
    answer = input(">>> ")
    try:
        answer = int(answer)
        if answer == (a*b):
            print("Good !")
            return True   
        else:
            print("Wrong, the answer was {}".format(a*b))  
            return False
    except ValueError:
        print("Error: Not an integer")
        return False

def AskDivision(max: int, minInt: int = 1) -> bool:
    a = random.randint(minInt, max)
    b = random.randint(minInt, max)

    print("What is the answer for {} / {}".format(a, b))
    answer = input(">>> ")
    try:
        answer = int(answer)
        if answer == int(a / b):
            print("Good !")
            return True   
        else:
            print("Wrong, the answer was {}".format(int(a/b)))  
            return False
    except ValueError:
        print("Error: Not an integer")
        return False

