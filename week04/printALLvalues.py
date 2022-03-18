# How to Print all the values in a loop instead of just the final answer
names = ['David', 'Peter', 'Michael', 'John', 'Bob']
for i in range (len (names)):
    print("{}.{}".format(i + 1, names[i]))