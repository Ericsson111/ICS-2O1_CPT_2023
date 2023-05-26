from Colors import *

def isInteger(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
        
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
        
def inputFloat(message):
    while True:
        result = input(message)
        if isFloat(result):
            result = float(result)
            break
        else: 
            print("Please enter a valid float value")
    return result 
    
def inputFloatLow(message,lowBound):
    while True:
        result = inputFloat(message)
        if result < lowBound: 
            print("Please enter a value larger than or equal to",lowBound)
        else: 
            break
    return result
    
def inputFloatHigh(message,highBound):
    while True:
        result = inputFloat(message)
        if result > highBound: 
            print("Please enter a value smaller than or equal to ",highBound)
        else: 
            break
    return result
    
def inputFloatBetween(message,lowBound,highBound):
    while True:
        result = inputFloat(message)
        if result < lowBound: 
            print("Please enter a value larger than or equal to ",lowBound)
        elif result > highBound: 
            print("Please enter a value smaller than or equal to ",highBound)
        else: 
            break
    return result
    
def inputInteger(message):
    while True:
        result = input(message)
        if isInteger(result):
            result = int(result)
            break
        else: 
            print("Please enter a valid integer value")
    return result 
def inputIntegerLow(message,lowBound):
    while True:
        result = inputInteger(message)
        if result < lowBound: 
            print("Please enter a value larger than or equal to",lowBound)
        else: 
            break
    return result
    
def inputIntegerHigh(message,highBound):
    while True:
        result = inputInteger(message)
        if result > highBound: 
            print("Please enter a value smaller than or equal to ",highBound)
        else: 
            break
    return result
    
def inputIntegerBetween(message,lowBound,highBound):
    while True:
        result = inputInteger(message)
        if result < lowBound: 
            print("Please enter a value larger than or equal to ",lowBound)
        elif result > highBound: 
            print("Please enter a value smaller than or equal to ",highBound)
        else: 
            break
    return result
    
def obtainYesNo(message):
    while True:
        result = input(message+"(y/n): ")
        if result == "y" or result == "n":
            break
    return result


def inputTravelDirection():
    while True:
        print(colors.reset)
        direction = input(colors.fg.yellow + "Which direction are you going? ")
        if direction.lower() in ['n', 'north']:
            return 'n'
        elif direction.lower() in ['s', 'south']:
            return 's'
        elif direction.lower() in ['w', 'west']:
            return 'w'
        elif direction.lower() in ['e', 'east']:
            return 'e'
        else:
            print(colors.fg.red + "Invalid direction input, please enter a valid direction.")
        print(colors.reset)
