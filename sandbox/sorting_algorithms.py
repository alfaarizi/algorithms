'''
A stable algorithm leaves the ‘like’ elements in the same order in the output array 
as they came in from the input array. As opposed to unstable, where the algorithm may mix ‘like’ elements. 
This is generally a non-issue, however it may be important for an algorithm to be stable, 
depending on the use of the sorted data set.

NOTE: 'like' means elements that are equal
'''


'''
Bubble sort cycles through the array of numbers, and looks at each pair of adjacent numbers. 
Bubble sort will then place the lower number on the left, towards the beginning of the array, 
and the higher number on the right, towards the end. 
This process is repeated and bubble sort will continue to loop through the array 
until no swaps are made, thus leaving a sorted array.
'''
def bubble_sort(arr): # O(n^2)
    '''
    repeatedly bubbles up the largest numbers to the end
    '''
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

'''
Selection sort works by splitting the input array into two parts: 
the list of numbers being built, from smallest to largest, 
and the remainder numbers that have yet to be sorted. 
Selection sort finds the smallest number from the unsorted list,
and places it at the end of the sorted one. Rinse and repeat.
'''
def selection_sort(arr): # O(n^2)
    '''
    selects the smallest numbers and place them at the beginning
    '''
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

'''
Insertion sort is similar to the previous two algorithms in that it’s big O notation is also quadratic, 
O(n²). Insertion sort works by building the final, sorted array one item at a time. 
The algorithm will iterate through the initial array, remove one element, 
and place it in its proper place as a part of the sorted list.
'''
def insertion_sort(arr): # O(n^2)
    '''
    NOTE:
    most used simple algorithm, because it's:
    - adaptive: efficiently sorts sorted data
    - stable: does not change the ORDER of 'like' elements in the array (not position)
    - online: can sort the area as it receives new items
    - in-place: requires small memory to run
    - simple implementation
    '''
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


'''
Merge sort operates by first breaking an array into its individual components. 
It then ‘pairs up’ an individual with another, putting them into their proper place (sorted) 
with reference to each other. Merge sort then continues to pair up each sublist of numbers 
and sort them in the process. This is continued until there is just one list remaining — the sorted array.
'''
def merge_sort(arr): # O(n log n)
    '''
    - divide-and-conquer algorithm
    - stable
    - requires a scaling amount of auxiliary processing power to work, gotta give the guy some space

    NOTE:
    'auxiliary processing' menas extra resources an algorithm needs beyond the input itself. 
    More formally, this is called auxiliary space or auxiliary memory.
    '''
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    res = []
    i = j = 0
    n_left, n_right = len(left), len(right)
    while i < n_left and j < n_right:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < n_left:
        res.append(left[i])
        i += 1
    while j < n_right:
        res.append(right[j])
        j += 1
    return res    


'''
Quicksort works by:
1. First selecting a pivot number in the array,
2. Then sorting the other numbers by placing them before or after the pivot number respectively.
3. At this point, the pivot number is in the correct location, and the two groups of numbers (one on each side of the pivot number) still need to be sorted.
4. New pivot numbers are then chosen within the remaining subsets, and this process is repeated until no swaps are made.
'''
def quick_sort(arr, left, right): # O(n^2), Theta(n log n)
    '''
    - effective for its speed and small amounts of additional memory needed
    - in its base form, is an unstable sorting algorithm
    - can be fast and highly efficient, given the right circumstances
    '''
    if left < right:
        pivot = _partition(arr, left, right)
        quick_sort(arr, left, pivot)
        quick_sort(arr, pivot+1, right)
    return arr

def _partition(arr, left, right):
    pivot = arr[left]
    i, j = left - 1, right + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


'''
Heapsort is, at its core, an upgraded version of selection sort. 
They are similar because heapsort breaks down the input data into two groups, 
sorted and unsorted, and builds the sorted group one number at a time

Where they differ, is where heapsort uses, a heap, to build the unsorted group 
so its not blindly finding each number, one at a time. Heapsort adds the largest number 
from the unsorted group to the sorted group, then rebuilds the heap and repeats the process, 
adding the highest number to the sorted group.
'''
def heap_sort(arr): # O(n log n)
    # Build heap
    n = len(arr)
    last_nonleaf_idx = n//2 - 1
    for i in range(last_nonleaf_idx, -1, -1): # start from bottom, work up to root (at i=0)
        _heapify_max(arr, n, i)

    # Sort elements, fix heap
    for i in range(n - 1, 0 , -1): # place n - 1 to the correct position, last element is auto correct
        arr[0], arr[i] = arr[i], arr[0]
        _heapify_max(arr, i, 0)

def _heapify_max(arr, heap_size, root_idx):
    maxi_root_idx = root_idx
    left, right = 2 * root_idx + 1, 2 * root_idx + 2 
    
    # Find the largest among root, left child, right child
    if left < heap_size and arr[left] > arr[maxi_root_idx]:
        maxi_root_idx = left
    if right < heap_size and arr[right] > arr[maxi_root_idx]:
        maxi_root_idx = right

    # If root is not the largest, swap and continue heapifying
    if maxi_root_idx != root_idx:
        arr[root_idx], arr[maxi_root_idx] = arr[maxi_root_idx], arr[root_idx]
        _heapify_max(arr, heap_size, maxi_root_idx) # Recursively fix the affected subtree
    


if __name__ == "__main__":
    ulst = [8,2,1,6,7]
    
    lst = ulst[:]
    bubble_sort(lst)
    print(lst)

    lst = ulst[:]
    selection_sort(lst)
    print(lst)

    lst = ulst[:]
    insertion_sort(lst)
    print(lst)

    lst = merge_sort(ulst[:])
    print(lst)

    lst = ulst[:]
    quick_sort(lst, 0, len(lst)-1)
    print(lst)

    lst = ulst[:]
    heap_sort(lst)
    print(lst)