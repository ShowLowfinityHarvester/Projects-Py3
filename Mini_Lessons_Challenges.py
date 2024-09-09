# These are school projects! Github page may be all cluttered until 2025 or 2026.

my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
cols = 3
rows = 4
usrint = int(input("What number do you want this list to be multiplied by? -> "))
for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] * usrint

print(my_list)