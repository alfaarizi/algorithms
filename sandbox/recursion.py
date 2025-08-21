'''
Recursions

When trying to figure out loop patterns, ask yourself a few questions first.
1. What's changing at each iteration?
   Is it an index going up, pointers moving aroujnd, or maybe items getting pulled off a stack?
   That changing thing usually becomes your function parameter in recursion
2. Look at when the loop stops
   That's your best case
3. Notice if you're building up some result as you go (like a sum) or just doing stuff without collecting anything
   That tells you whether you need to combine return values or just make simple recursive calls
'''

def quick_sort_iterative(arr, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.append((low, pivot))
            stack.append((pivot+1, high))

def quick_sort_recursive(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort_recursive(arr, low, pivot)
        quick_sort_recursive(arr, pivot+1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i, j = low - 1, high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left)//2    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right) # important return
    else:
        return binary_search_recursive(arr, target, left, mid-1)

if __name__ == "__main__":
    ls = [8, 2, 6, 1, 3]

    quick_sort_recursive(ls, 0, len(ls)-1)

    res = binary_search_recursive(ls, 8, 0, len(ls)-1)
    assert res == len(ls)-1, res

    print(ls)