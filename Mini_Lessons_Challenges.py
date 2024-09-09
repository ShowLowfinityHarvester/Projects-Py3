# These are school projects! Github page may be all cluttered until 2025 or 2026.

my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]
cols = 3
rows = 5

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] + 3

print(my_list)