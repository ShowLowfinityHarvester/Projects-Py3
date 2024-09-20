# These are school projects! Github page may be all cluttered until 2025 or 2026.
def selection_sort(arr):
    for i in range(len(arr)):
        smaller_i = i
        for j in range(i+1, len(arr)):
            if arr[smaller_i] > arr[j]:
                smaller_i = j
        if smaller_i != i:
            arr[i], arr[smaller_i] = arr[smaller_i], arr[i]

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]

inum = int(input("Please Input a Number -> "))
arr.append(inum)
selection_sort(arr)
print(arr)