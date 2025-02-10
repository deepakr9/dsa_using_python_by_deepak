
def linear_search(arr, tar):
    if not arr:
        return False
    for i in range(len(arr)):
        if arr[i] == tar:
            return True
    return False


arr = [x*x for x in range(10, 12)]
tar = 121
res = linear_search(arr, tar)
if res:
    print("Target exists in an array")
else:
    print("Target was not in an array")