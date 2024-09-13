# These are school projects! Github page may be all cluttered until 2025 or 2026.

flowers = [int(n) for n in input("How many blossoms are on each tree? -> ").split()]

def beetree(flowers):
    if len(flowers) == 1:
        bee = flowers[0] * 3
        print(bee)
    else:
        middle = len(flowers) // 2
        first_half = flowers[:middle]
        second_half = flowers[middle:]

        beetree(first_half)
        beetree(second_half)

    
beetree(flowers)