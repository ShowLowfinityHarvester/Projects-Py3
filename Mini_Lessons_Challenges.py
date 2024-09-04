# These are school projects! Github page may be all cluttered until 2025 or 2026.
while True:
    try: 
        rows = int(input("Enter in a number! -> "))
        break
    except ValueError:
        print("Please enter in a number. Don't enter in commas")
rowlist = [1, 2, 3, 4, 5]
list = [[j*rows for j in rowlist] for i in range(rows)]
print(list)