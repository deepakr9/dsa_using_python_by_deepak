def bubble_sort(arr):
    N = len(arr)

    for i in range(N):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = list(map(int, input().split()))

res = bubble_sort(arr)
print(res)
