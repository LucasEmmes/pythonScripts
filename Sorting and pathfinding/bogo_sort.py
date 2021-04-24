import random

def scramble(arr):
    scrambled = []
    while len(arr) > 0:
        scrambled.append(arr.pop(random.randint(0, len(arr)-1)))

    return scrambled

def check_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
        
    return True

def bogo_sort(arr):
    c = 0
    while not check_sorted(arr):
        arr = scramble(arr)
        c+=1

    print(f"Took {c} rounds")   # Just for fun, to show the inconsistency
    return arr                  # of this sorting """"algorithm""""

# Whoever came up with this deserves to
# stub their toe more frequently than normal
