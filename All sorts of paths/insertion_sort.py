def insertion_sort(arr):
    for j in range(1, len(arr)):
        current_val = arr[j]
        i = j-1
        while i >= 0 and arr[i] > current_val:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = current_val
    return arr
