# 5) Numbers below 13 are spelled out 
import re 

# Captures every number, and allow for possible decimal numbers
numberpattern = re.compile(r'\d+\.?\d*')


def spelloutnumbers(testword):
    passed = True
    # Loop through each number found, checking if less than 13, or a negative number
    for match in re.finditer(numberpattern,testword):
        # Convert string to a float, then convert to decimal which removes any decimal places 
        currentnumbermatch = int(float(match.group()))
        currentnumberlocation = match.start()
        if  currentnumbermatch < 13 or str(testword)[currentnumberlocation - 1: currentnumberlocation] == "-":
            passed = False
            break

    return passed
