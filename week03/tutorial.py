##rounding a number 
#notRoundednumber = float(input('Enter a number with 2 decimal places'))
#roundedNumber = int(round(notRoundednumber))
#print('{} is then rounded to {}' .format(notRoundednumber,roundedNumber))

## getting the absolute value of a number
#notAbsolutevalue = int(input('Chose a number that is negative'))
#absoluteValue = int(abs(notAbsolutevalue))
#print('{} is the absolute value of {}' .format(absoluteValue, notAbsolutevalue))

## how to round down a number

from importlib import import_module
import math


#numberTofloor = float(input("Enter a float number:"))
#flooredNumber = abs(math.floor(numberTofloor))
#print('{} floored is {}'.format(numberTofloor, flooredNumber))

orginalNumber = float(input('This is how much is deposited: '))
countedNumber = abs(int(100*orginalNumber))
print("I deposited {} but the bank logdged {}" .format(orginalNumber, countedNumber))