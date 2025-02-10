def binary_search(arr, target):
    if not arr:
        return False
    n = len(arr)
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return False

arr = [x*x for x in range(10, 12)]
print(arr[len(arr)//2])
tar = 121
res = binary_search(arr, tar)
print(res)
if res:
    print("Target exists in an array")
else:
    print("Target was not in an array")