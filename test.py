def median(arr):
    n = len(arr)
    arr.sort()
    if n % 2 == 1:
        return arr[n//2]
    else:
        return (arr[int(n/2) - 1] + arr[int(n/2)])/2

def Q1(arr):
    n = len(arr)
    less_than = arr[n // 2:]
    print(less_than)
    return median(less_than)

print(Q1([3,4,5,6,7,4,67,7,4]))