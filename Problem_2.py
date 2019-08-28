'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

'''
def prod(arr,n):
    left = [1] * n
    right = [1] * n
    for i in range(1,n):
        left[i]=left[i-1]*arr[i-1]
    # print("left",left)
    for i in range(n-2,-1,-1):
        right[i]=right[i+1]*arr[i+1]
    # print("right",right)
    prod = [1]*n
    for i in range(n):
        prod[i] = left[i]*right[i]
    # print("prod",prod)
    return prod

arr = [1, 2, 3, 4, 5]
res = prod(arr,len(arr))
print(res)

'''
Time Complexity is O(n)
'''