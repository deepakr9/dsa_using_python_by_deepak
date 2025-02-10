def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        k = i

        for j in range(i+1, n):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]

    return arr

arr = list(map(int, input().split()))

res = selection_sort(arr)
print(res)