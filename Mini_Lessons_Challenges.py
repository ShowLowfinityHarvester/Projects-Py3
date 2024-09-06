# These are school projects! Github page may be all cluttered until 2025 or 2026.

cols = ["apple", "grape", "peach", "cinnamon", "vanilla"]
rows = input("Input a list of fruits -> ").split()
lists = []
for i in rows:
    col = []
    for j in cols:
        col.append(i + " " + j)
    lists.append(col)
print(lists)