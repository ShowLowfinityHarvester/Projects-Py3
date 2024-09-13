# These are school projects! Github page may be all cluttered until 2025 or 2026.

n = int(input("Number -> "))
def fact(jay):
    if jay <= 1:
        return 1
    else:
        return jay * (fact(jay-1))
print(fact(n))