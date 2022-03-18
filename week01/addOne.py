#read in a number and add one
#Author: Megan 
from unicodedata import numeric


number = input('please enter a number:')
newnumber = int(number) +1
print('{} plus one is {}'.format(number, newnumber))