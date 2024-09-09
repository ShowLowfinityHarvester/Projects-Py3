# These are school projects! Github page may be all cluttered until 2025 or 2026.

# Opening, Printing, and closing a file
file = open("example.txt", "r") # "r" reads the text file
print(file.read())
file.close()

# Reading Parts of a file

file = open("example.txt", "r")
print(file.read(10)) # Prints out the first 10 characters
print(file.readline()) # Prints out a line of text in the file
print(file.readline())
print(file.readlines()) # Returns all the lines in a file as a list with each being a line
file.close()

# Opening, Writing (adding text), Overrwiting and printing a file

file = open("example.txt", "a")  # "a" Appends a line to the text file
file = open("example.txt", "w")  # "w" Replaces everything in a text file. This can also be used to create a new text file!
file.write("I love programming!")
file.close()

file = open("example.txt", "r")
print(file.read())

# Nested For Loops

list = ["hello" for i in range(5)] 
print(list) # This code creates a list 5 indexes long, with "hello" as the value in all indexes (1D 1 line)

rows = 3 
pets = ["str1", "str2", "str3", "str4", "str5"]
list = [[j for j in pets] for i in range(rows)]
print(list) # Same thing as the 1D list above but in 2D

# Multi-Dimensional Lists

rows = 5
cols = 3
list = []
for x in range(rows):
    col = []
    for y in range(cols):
        list.append(5)
        print(list) # 2d list with 5 rows and 3 columns

# Iterating Through 2D Lists

my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]
cols = 3
rows = 5

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] + 3 # This function interates through the 2d list and adds 3 to all items in the list

print(my_list)