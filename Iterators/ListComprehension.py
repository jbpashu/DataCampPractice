#How would a list comprehension that produces a list of the first character of each string in doctor look like? Note that the list comprehension uses doc as the iterator variable. What will the output be?
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

[doc[0] for doc in doctor]

#You know that list comprehensions can be built over iterables. Given the following objects below, which of these can we build list comprehensions over?

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

range(50)

underwood = 'After all, we are nothing more or less than what we choose to reveal.'

jean = '24601'

flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

valjean = 24601

# Interger objects are not interable

#write a list comprehension that produces a list of the squares of the numbers ranging from 0 to 9
squares = [i * i for i in range(0, 10)] # Last number excluded we need to till 9 but passing 10 will give the desired o/p

print(squares)

#matrix = [[0, 1, 2, 3, 4],
#          [0, 1, 2, 3, 4],
#          [0, 1, 2, 3, 4],
#          [0, 1, 2, 3, 4],
#          [0, 1, 2, 3, 4]]
# Your task is to recreate this matrix by using nested listed comprehensions
#[[output expression] for iterator variable in iterable]

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0, 5)] for col in range(0, 5)]

# Print the matrix
for row in matrix:
    print(row)

    
