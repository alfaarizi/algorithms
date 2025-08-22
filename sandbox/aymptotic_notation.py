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
- pattern: 
    - direct access,
    - simple arithmetic, OR
    - fixed number of operations
i.e., acccesssing element in an array
'''
def get_elem(ls, i):
    return ls[i]

'''
O(log n): Logarithmic time
- algorithm that grows logarithmatically with the input size
- pattern: 
    - repeatedly reduces problem size by a constant factor (usually half), OR
    - navigate tree structures of height log n
i.e., binary search in a sorted array, tree traveral of specific depth
'''
def binary_search(sorted_ls, target):
    """
    we make binary decisions at each step, is the midpoint bigger or smaller than target?
    """
    # (left+right)/2 = left/2 + right/2 = right/2 - left/2 + left = left + (right-left)/2 => prevents integer overflow
    left, right = 0, len(sorted_ls)-1
    while left <= right:
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
- patterns: 
    - single pass through data, visiting each element exactly once
NOTE: "pass" means going through the data structure from beginning to end
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
- patterns: 
    - divide-and-conquer with O(n) work at each step, OR
    - perform O(log n) operation for each n elements
- i.e., sorting algorithms like merge sort, heap sort, and quick sort (average)
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
- algorithm that grows quadratically with the input size
- patterns:
    - nested loops that both depend on input size, OR
    - compare every pair of elements
i.e., bubble sort and insertion sort
'''
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

def insertion_sort(lst):
    i = 1
    while i < len(lst):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
                j -= 1
        i += 1

'''
O(2^n): Exponential time
- algorithms that grows exponentially with the input size
- patterns: 
    - generate all possible subsets/combination,
    - make binary choices at each step AND explore all possibilities
    - recursive algorithms that branch into 2 calls without memoization
i.e., recursive algorithms for fibonacci sequence

NOTE: 
1. Memoization is an optimization technique that stores the results of a function call in a cache,
then returns the cached result when the function is called with the same parameters again

2. Brute force is a problem-solving aproach that tries every possible solution until it finds the right one. 
The key characteristics are:
- Exhaustive search: checks all possibilities
- No pruning: does not skip obviously bad solutions
- Naive: most straightforward method
- Complete enumeration: generate/test all combination
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

'''
O(n!): Factorial time
- algorithms that grows factorial time with the input size
- patterns: 
    - generate all possible arrangements/orderings of n items, typically using backtracking

NOTE: 
1. backtracking is an algorithm that explores all possible solutions by making choices, and 
when a choice leads to a dead end or you've fully explored that path, you "undo" the choice and
try the next option
i.e., agorithms that generate all permutations of a string
'''
def permute(str, left, right, res):
    if left == right:
        res.append(str)
    else:
        for i in range(left, right+1):
            str = swap(str, left, i)
            permute(str, left+1, right, res)
            str = swap(str, left, i)
        

def swap(str, i, j):
    '''
    objects are always passed by reference. 
    - if an object is mutable, then any changes to the object is reflected outside the function scope
    - if an object is immutable, it cannot be modified. To get 'reflective' changes, create a new object and reassign the variable outside the function scope
    '''
    if i == j:
        return str
    elif i > j:
        i, j = j, i
    return str[:i] + str[j] + str[i+1:j] + str[i] + str[j+1:]

def time_algorithms():
    import timeit
    
    ls = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 30]

    all_time = {}

    shared = {
        **globals(),
        'ls':ls
    }

    # Binary Search (need sorted list)
    t = timeit.timeit('binary_search(ls, 50)', globals=shared, number=100_000)
    all_time.update({'binary_search': t})

    # Find Max
    t = timeit.timeit('find_max(ls)', globals=shared, number=100_000)
    all_time.update({'find_max': t})

    # Merge Sort
    t = timeit.timeit('merge_sort(ls[:])', globals=shared, number=10_000)
    all_time.update({'merge_sort': t})
    
    # Insertion Sort
    t = timeit.timeit('insertion_sort(ls[:])', globals=shared, number=10_000)
    all_time.update({'insertion_sort': t})
    
    # Quick Sort
    t = timeit.timeit('temp = ls[:]; quick_sort(temp, 0, len(temp)-1)', globals=shared, number=10_000)
    all_time.update({'quick_sort': t})

    # Merge Arrays
    t = timeit.timeit('merge([25, 50, 76], [12, 34, 88])', globals=shared, number=100_000)
    all_time.update({'merge': t})
    
    # String Swap
    t = timeit.timeit('swap("ALGORITHM", 1, 4)', globals=shared, number=100_000)
    all_time.update({'swap': t})
    
    # Permutations (using smaller string)
    t = timeit.timeit('res = []; permute("ABCD", 0, 3, res)', globals=shared, number=100)
    all_time.update({'permute': t})

    '''
    {
        "binary_search": 0.030827000009594485,
        "find_max": 0.03251908300444484,
        "merge_sort": 0.0510970419854857,
        "insertion_sort": 0.02584241598378867,
        "quick_sort": 0.03485125000588596,
        "merge": 0.05001924998941831,
        "swap": 0.022615583991864696,
        "permute": 0.0013292919902596623
    }
    '''

    import json
    print(json.dumps(all_time, indent=3))

if __name__ == "__main__":

    time_algorithms()

    # ls = [1,2,3,5,8,9,14]
    # ls_2 = [8,2,1,6,7]
    # ls_descending = [3,5,4,7]
    # ls_empty = []
    # assert binary_search(ls, 9) == 5

    # assert find_max(ls_2) == 8

    # # original arr
    # prev_ls_2 = ls_2[:]

    # ls_2 = merge_sort(ls_2)
    # assert ls_2 == sorted(prev_ls_2)

    # ls_2 = prev_ls_2[:]
    # insertion_sort(ls_2)
    # assert ls_2 == sorted(prev_ls_2)

    # merged_lst = merge([2,8], [1,6,7])
    
    # prev_ls_2 = ls_2[:]
    # sorted_ls_2 = merge_sort(ls_2)
    # assert sorted_ls_2 == sorted(prev_ls_2)

    # quick_sort(ls_descending, 0, len(ls_descending)-1)

    # str = "ABCDEF"

    # str = swap(str, 1, 1)

    # res = []
    # str = permute(str, 0, len(str)-1, res)