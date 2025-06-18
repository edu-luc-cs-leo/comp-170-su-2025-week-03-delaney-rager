# Reflection for Previous Week's Homework

An f-string is a formatted string (or a fancy string). Essentially it functions to incorporate variables or function outputs into a string. We can use f-strings to embed variables in strings and we can also specify characteristics of variables. For example: f'Hello, {name}.' Where this f-string allows us to use a variable that can change in a string format that won't change. Another example: f'The cost is {cost:.2f}'. In this f-string, not only do we embed a variable 'cost', we also specify to truncate its decimal to two places.

A for-loop iterates over a range of numbers or a list. Essentially, a for loop calls on some variable that represents an index of the count of the for loop or where we are in a list. An example: 
length = 5
count = 0
for i in range(length):
    count = count + 1
This for loop returns the number of loops the for loop does until it reaches the end value of range(length) by counting each time. Another example:
list = [1,2,3]
for i in list:
    print(i)
Each iteration in this for loop will retrieve the specific number it is indexed to and print that.

As for my assignment last week, I executed the function greet, the list of names, and the function greet_friends fairly well. As for the solve_quadratic there were a few things that I could have done better. I should have imported math in order to do the square root function, however, I just raised the discriminant to the power of 0.5. I should also of just used a variable for the discriminant throughout the computation so that the computer does not have to more evaluations than needed.