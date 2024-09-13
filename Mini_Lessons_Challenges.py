# These are school projects! Github page may be all cluttered until 2025 or 2026.

this_list = ['panda', 'lion', 'giraffe', 'tiger', 'elephant', 'monkey', 'fish', 'snake', 'bearded dragon', 'koala']

def feeding(this_list):
    if len(this_list) == 1:
        animal = this_list[0]
        print(f"The {animal} has been fed")
    else:
        middle = len(this_list) // 2
        first_half = this_list[:middle]
        second_half = this_list[middle:]

    feeding(first_half)
    feeding(second_half)
    feeding(this_list)