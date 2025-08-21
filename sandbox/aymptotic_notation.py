'''
A symptotic notation describes the complexity of an algorithm in terms of its behavior as the input grows.

There three most common notations are:

Big O Notation
- Describes the upper bound of an algorithm's time and space
- Provides worst-case scenario, meaning the maximum time and space the algo will require

Omega Notation
- Describes the lower bound of an algorithm's time and space
- Provides the best-case scenario, mining the minimum time and spave the algo will require

Theta Notation
- Describes the exact bound of an algorithms' time and space
- Provides the average-case scenario

# Common runtimes, sorted by the least time
- O(1)
- O(log n)
- O(n)
- O(n log n)
- O(n^2)
- O(2^n)
- O(n!)
'''

# Examples

'''
O(1): Constant time
- algorithm that takes a constant time (to complete) regardless of the input size
- pattern: direct accesss/calculation
i.e., acccesssing element in an array
'''
def get_elem(ls, i):
    return ls[i]

'''
O(log n): Logarithmic time
- algorithm that grows logarithmatically with the input size
- pattern: it cuts the problem size in half at each iteration, then does O(1) operations
i.e., binary search in a sorted array
'''
def binary_search(sorted_ls, target):
    """
    we make binary decisions at each step, is the midpoint bigger or smaller than target?
    """
    # (left+right)/2 = left/2 + right/2 = right/2 - left/2 + left = left + (right-left)/2 => prevents integer overflow
    left, right = 0, len(sorted_ls)-1
    while left < right:
        mid = left + (right-left)//2
        if sorted_ls[mid] == target:
            return mid
        elif sorted_ls[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

'''
O(n): Linear time
- algorithm that grows linearly with the input size
- patterns: single loop through data, visiting each element once
i.e., finding the maximum element in an array
'''
def find_max(ls):
    if not ls:
        return None
    n = len(ls)
    max = ls[0]
    for i in range(n):
        if (ls[i] > max):
            max = ls[i]
    return max

'''
O(n log n): Log-linear time
- algorithms that grows significantly faster than linear but much slower than quadratic with the input size
- patterns: it cuts the problem size in half at each iteration, then does O(n) operations
- i.e., sorting algorithms like merge sort and quick sort
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0
    len_left, len_right = len(left), len(right)
    while i < len_left and j < len_right:
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len_left:
        res.append(left[i])
        i += 1
    while j < len_right:
        res.append(right[j])
        j += 1
    return res

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot)
        quick_sort(arr, pivot+1, high)
    return arr

# [3,5,2,4,3,5,6]
def partition(arr, low, high):
    '''
    requirements: arr[i] < pivot, arr[j] > pivot
    '''
    pivot = arr[low]
    i, j = low-1, high+1
    while True:
        i+=1
        while arr[i] < pivot:
            i+=1
        j-=1
        while arr[j] > pivot:
            j-=1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


'''
O(n^2): Quadratic time
'''

'''
O(2^n): Exponential time
'''

'''
O(n!): Factorial time
'''

if __name__ == "__main__":
    ls = [1,2,3,5,8,9,14]
    ls_2 = [8,2,1,6,7]
    ls_descending = [3,5,4,7]
    ls_empty = []
    assert binary_search(ls, 9) == 5

    assert find_max(ls) == 14

    prev_ls = ls[:]
    merge_sort(ls)

    assert ls == sorted(prev_ls)

    merged_lst = merge([2,8], [1,6,7])
    
    prev_ls_2 = ls_2[:]
    sorted_ls_2 = merge_sort(ls_2)
    assert sorted_ls_2 == sorted(prev_ls_2)

    quick_sort(ls_descending, 0, len(ls_descending)-1)