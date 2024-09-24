# These are school projects! Github page may be all cluttered until 2025 or 2026.

answer = int(input("Enter a number between 0 - 100 -> "))

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
arr.append(answer)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]
        mergeSort(Left)
        mergeSort(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

mergeSort(arr)
print(arr)