def check_validity(arr):
    for tower in arr:
        for i in range(len(tower)-1):
            if tower[i] > tower[i+1]:
                return False
    return True

def check_formatting(arr):
    tower_size = -1
    for tower in arr:
        if tower_size == -1:
            tower_size = len(tower)
        elif len(tower) != tower_size:
            return False
        
    return True

def formatted_tower(arr):
    pass

def generate_hanoi_tower(size):
    pass

def move_piece(arr, piece, place, print_steps=False):
    # For visual purposes
    if print_steps: print(arr)
    # Remove piece from the tower it's currently in
    for tower in arr:
        try:
            i = tower.index(piece)
            tower[i] = 0
        except:
            pass

    # Move to the tower it should be in
    tower_dest = arr[place]
    for i in range(len(tower_dest)):
        if tower_dest[i] != 0:
            tower_dest[i-1] = piece
            break
        elif i == len(tower_dest)-1:
            tower_dest[-1] = piece

    return arr

def build_tower(arr, size, place, print_steps=False):

    # Check that nothing has gone wrong
    if not (check_validity(arr) and check_formatting(arr)):
        print("SOMETHING IS WRONG")
        raise ValueError("BREUH")

    # If minimal tower
    if size == 1:
        return move_piece(arr, 1, place, print_steps=print_steps)

    # If not a minimal tower
    # Find out where piece 'size' is located
    size_pos = 0
    for i in range(len(arr)):
        if size in arr[i]:
            size_pos = i
            break
    
    # Build a tower of size ('size' - 1) at location {0,1,2}/{size_pos, place} i.e. the free temporary tower
    places = [0,1,2]
    places.remove(place)
    places.remove(size_pos)

    # Move away all pieces on top of me by building tower of size ('size'-1) on the temp tower
    arr = build_tower(arr, size-1, places[0], print_steps=print_steps)
    # Move myself
    arr = move_piece(arr, size, place, print_steps=print_steps)
    # Move back all pieces to be on top of me by building tower of size ('size'-1) on myself
    arr = build_tower(arr, size-1, place, print_steps=print_steps)

    return arr



hanoi = [[1,2,3,4], [0,0,0,0], [0,0,0,0]]
print(build_tower(hanoi, 4, 2, print_steps=True))