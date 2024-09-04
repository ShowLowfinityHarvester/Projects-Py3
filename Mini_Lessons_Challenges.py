# These are school projects! Github page may be all cluttered until 2025 or 2026.

weather = input("List of weather? -> ").split()
rowlist = ["windy", "breezy", "calm"]
list = [[(y + " " + x) for x in rowlist] for y in weather]
print(list)