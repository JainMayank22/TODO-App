def balancedArr(arr):
    sum_left, sum_right = 0, sum(arr[1:])
    for i in range(len(arr)-1):
        sum_left += arr[i]
        sum_right -= arr[i+1]
        if sum_left == sum_right:
            return i+1
    return -1
 