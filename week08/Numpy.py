import numpy as np

listOfNumbers = [1,2,3,4,5,6]
numbers = np.array([1,2,4,5])

## Adds 3 to each number in the array
#numbers = numbers +3 
## Also can multiply 
#numbers = numbers *3 

## Too multiply by another array 
numbers = numbers * np.array([1,4,5,6])


print(numbers)
print(listOfNumbers)

## To get random numbers use np.random, since we want numbers we use randint which looks for 3 values 
## randint(a,b,n) a= the starting number, b = end number and n is the number of values you want
## So we want 5 random numbers between 100 and 200
randomNumbers = np.random.randint(100,200,5)
print(randomNumbers)