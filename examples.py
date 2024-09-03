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

# Nested For Loops (this is gonna be a hard one!!!)