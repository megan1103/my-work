# Programming and Scripting
# Problem Set 1
# Week 2
# Author: Megan O'Donovan

weight = int(input('Enter weight(kg):'))
height = int(input('Enter height(cm):'))
# BMI is measured using kg and meters squared - height measured in cm must be changed 
newheight = (height/100)**2
# round to 2 decimal places
bmivalue = round(weight/newheight,2)
print('The BMI is (kg/m^2) {}.' .format(bmivalue))