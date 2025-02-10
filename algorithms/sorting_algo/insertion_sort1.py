def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

arr = list(map(int, input().split()))

res = insertion_sort(arr)
print(res)