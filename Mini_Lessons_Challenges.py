# These are school projects! Github page may be all cluttered until 2025 or 2026.

while True:
    try:
          ABQ = int(input("Please input a number! -> "))
          break 
    except ValueError:
         print("Please enter in a number.")

file = open("example.txt", "r")
print(file.read(ABQ))
file.close()