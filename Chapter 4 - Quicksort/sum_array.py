def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

print(sum([1,3,6,8]))

#Use of Recursion
def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

print(sum([1,3,6,8]))