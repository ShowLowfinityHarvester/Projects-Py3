# These are school projects! Github page may be all cluttered until 2025 or 2026.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        val_to_insert = arr[i]
        insert_spot = i
        while insert_spot > 0 and arr[insert_spot - 1] > val_to_insert:
            arr[insert_spot] = arr[insert_spot - 1]
            insert_spot -= 1

        arr[insert_spot] = val_to_insert

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

inum = int(input("Please Input a Number -> "))
arr.append(inum)
insertion_sort(arr)
print(arr)