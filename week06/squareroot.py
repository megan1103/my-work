#def my_function(fname):
#  print(fname + " Refsnes")

#my_function("Emil")
#my_function("Tobias")
#my_function("Linus")

#def my_function(*kids):
#  print("The youngest child is " + kids[0])
### kids[1] is based on the order of names below 0=Emil, 1=Tobias and 2 = Linus
#my_function("Emil", "Tobias", "Linus")

#def my_function(food):
#  for x in food:
#    print(x)

#fruits = ["apple", "banana", "cherry"]

#my_function(fruits)

#def my_function(x):
#  return 5 * x

#print(my_function(3))
#print(my_function(5))
#print(my_function(9))

#from unittest import result


def your_sqrt(y: float) -> float:
    x: float = y
    for _ in range(0,7):
        x = x - (x*x-y)/(2*x)
    return x
finalValue = input
print(your_sqrt(145))

#def your_sqrt(y: float) -> float:
#    x: float = y
#    if(x > 0):
#        result = x - (x*x-y)/(2*x)
#        print(result)
#    else:
#        result = 0
#    return result
#print(your_sqrt(4))