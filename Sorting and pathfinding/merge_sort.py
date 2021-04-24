def merge(a, b):
    result = []
    a.append(float('inf'))
    b.append(float('inf'))

    while len(a) > 1 or len(b) > 1:
        if a[0] <= b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
            
    return result

def merge_sort(arr):
    """
    Merge sort just like you remember it from your college classes
    """
    if len(arr) == 1:
        return arr

    a = merge_sort(arr[:len(arr)//2])
    b = merge_sort(arr[len(arr)//2:])

    return merge(a,b)
