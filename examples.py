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
        my_list[i][j] = my_list[i][j] + 3 # This function interates through the 2d list and adds 3 to all items in the list, my_list[i][j] represents every single item in the list in turn.

print(my_list)

# Object-Oriented Programming

class dog: # Class function is a blueprint of an object (outline)
    def __init__(self, name, color, size): # Initialize The class **Has to be def __init__(self)! 
        self.name = name
        self.color = color
        self.size = size


# Creating an instance

class Hat: # everything from OOP from above stays the same
    def __init__(self, kind, color, material):
        self.kind = kind
        self.color = color
        self.material = material

myObject = Hat("ABQ Isotopes Hat", "Red", "Felt") # Adding the instance

# Objects Continued

class Vacation:
    def __init__(self, place, distance, weather):
        self.place = place
        self.distance = distance
        self.weather = weather


    def tuesday(self): # Object Method
        print("We will be hiking on Tuesday.")

summer = Vacation("Hawaii", 2000, "Sunny")
summer.rating = 10 # Adding an attribute
summer.weather = "rainy" # Modifying the object propertiesS
print(summer)
print(summer.rating)
print(summer.weather)

# stacks

stack = []

stack.append('WXJ34')
stack.append('WXL90')
stack.append('WXJ38')
stack.append('WWG36')

stack.pop()

print(stack)

# Recursion

this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']

def feeding(this_list):
    if len(this_list) == 1:
        animal = this_list[0]
        print(f"The {animal} has been fed")
    else:
        middle = len(this_list) // 2
        first_half = this_list[:middle]
        second_half = this_list[middle:]

    feeding(first_half)
    feeding(second_half)
    feeding(this_list)

# Recursion vs. Iteration

n = int(input("Number -> "))
def fact(jay):
    if jay <= 1:
        return 1
    else:
        return jay * (fact(jay-1))
print(fact(n)) # This is a recursive factorial function

# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

inum = int(input("Please Input a Number -> "))
arr.append(inum)
bubble_sort(arr)
print(arr)

# Selection Sort

# sdd

# Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val_to_insert = arr[i]
        insert_spot = i
        while insert_spot > 0 and arr[insert_spot - 1] > val_to_insert:
            arr[insert_spot] = arr[insert_spot - 1]
            insert_spot -= 1

        arr[insert_spot] = val_to_insert

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

inum = int(input("Please Input a Number -> "))
arr.append(inum)
insertion_sort(arr)
print(arr)

# Merge Sort

# These are school projects! Github page may be all cluttered until 2025 or 2026.

answer = int(input("Enter a number between 0 - 100 -> "))

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(answer)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]
        mergeSort(Left)
        mergeSort(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

mergeSort(arr)
print(arr)