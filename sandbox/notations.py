
def test_slice_notation():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr[2:5] # from index 2 to 4
    arr[1:8:2] # from 1 to 7, step by 2
    arr[:4] # from start to index 3
    arr[6:] # from index 6 to end
    arr[:] # entire list
    arr[-3:] # last 3 elements
    arr[:-2] # all except last 2
    arr[-4:-1] # from 4th last to 2nd last
    arr[::2] # every 2nd element
    arr[1::2] # every 2nd, starting at 1
    arr[::-1] # reverse
    arr[::3] # every 3rd element