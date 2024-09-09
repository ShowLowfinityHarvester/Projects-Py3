# These are school projects! Github page may be all cluttered until 2025 or 2026.

x = int(input("What is the first number? -> "))
y = int(input("What is the second number? -> "))
z = int(input("What is the third number?-> "))
my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]
cols = 3
rows = 4
maxval = max(max(row) for row in my_list)
for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j]

print(maxval)