from numpy import insert

weekEnds = ("Saturday", "Sunday")
s = input("Please enter the day: ")
if s in weekEnds:
     print('It is the weekend, yay!')
else:
     print('Yes, unfortunately today is a weekday.')