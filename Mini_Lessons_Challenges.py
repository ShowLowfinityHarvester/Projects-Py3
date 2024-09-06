# These are school projects! Github page may be all cluttered until 2025 or 2026.

cols = [2, 5, 10, 100]
rows = [int(n) for n in input("Input a list of numbers -> ").split()]
lists = []
for i in rows:
    col = []
    for j in cols:
        col.append(i - j)
    lists.append(col)
print(lists)