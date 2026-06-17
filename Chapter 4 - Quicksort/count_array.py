def count(arr):
    cnt = 0
    for i,x in enumerate(arr):
        cnt = i + 1
    return cnt

print(count([1,3,6,8]))

#Use of Recursion
def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

print(count([1,3,6,8]))