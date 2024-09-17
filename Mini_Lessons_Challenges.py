# These are school projects! Github page may be all cluttered until 2025 or 2026.

def bubbleSort(sort_list):
    n = len(sort_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]