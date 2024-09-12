# These are school projects! Github page may be all cluttered until 2025 or 2026.

class Shopping:
    def __init__(self, item, quality):
        self.item = item
        self.quality = quality
        self.total = []

    def spending(self, cost):
        self.total.append(cost)

sportStore = Shopping("Kayak", "High Quality")
sportStore.spending(100)
sportStore.spending(94)
sportStore.spending(34)
print(sportStore.total)