my_list = [1, 2, 3, 4, 5]
sumTotal = 0
#For loops: is used top perform an action for each item in a list (or other iterable types like strings, tuples, etc)
for number in my_list:
    sumTotal += number
print("The sum is:", sumTotal)

# Example with string list
fruits = ["Apples","Bananas", "Cherries", "Dates"]
for fruit in fruits:
    print("I like", fruit)

# Examples with a range of numbers
for number in list(range(1, 10)):
    print("Number:", number)

# Examples with a range of numbers, asingnig index to each number
for index,number in enumerate(list(range(1, 10))):
    print("Index: ", index , "Number:", number)
