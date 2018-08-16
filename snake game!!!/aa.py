width = 4
height = 4
length = width * height

def at(board, pos):
    """Return 1 if there is a mole at the specified position, otherwise return 0."""
    return (board >> pos-1) & 1

def toggle(board, pos):
    """Hide the mole if there is one at the given position, otherwise pop it up. Return the resulting board."""
    if pos >= 1 and pos <= length:
        board ^= (1 << pos-1);
    return board;

def hit(board, pos):
    """Hit the mole at the given position and return the resulting board."""
    for i in [pos, pos+width, pos-width]:
        board = toggle(board, i)
    # avoid toggling some positions when edge of board is hit
    if pos % width != 0:
        board = toggle(board, pos+1)
    if pos % width != 1:
        board = toggle(board, pos-1)
    return board

def moles(board):
    """Return the positions of the moles."""
    return (pos for pos in range(1, length+1) if at(board, pos))

def board_from_moles(moles):
    """Return a board with the given positions of the moles."""
    board = 0
    for mole in moles:
        board = toggle(board, mole)
    return board

def depth_first(board, depth):
    """Depth-first search to a prespecified depth. Return a solution, if one is found, otherwise return False."""
    for mole in moles(board):
        new_board = hit(board, mole)
        if new_board == 0:
            return (mole,)
        elif depth > 0:
            result = depth_first(new_board, depth-1)
            if result:
                return (mole,) + result 
    return False

def search(board):
    """Perform depth-first search and return a solution, if one is found.
    Keep increasing the depth of the search, until a solution is found."""
    depth = 0
    while True:
        result = depth_first(board, depth)
        if result:
            return result
        else:
            depth += 1

def whack(initial_moles):
    """Whack 'em 'n crack 'em."""
    return search(board_from_moles(initial_moles))

def display(board):
    """Display the board to human."""
    for i in range(height-1, -1, -1):
        print(' '.join(['O' if at(board, i * width + j) else '-' for j in range(1, width+1)]))
    print("")

def test():
    """Some tests."""
    assert list(moles(board_from_moles([1,4,8,11]))) == [1,4,8,11]
    assert list(moles(hit(board_from_moles([1,2,4,8,9,10,11,14]), 10))) == [1,2,4,6,8]
    assert list(moles(hit(board_from_moles([3,4,8]), 4))) == []
    assert list(moles(hit(board_from_moles([5,6,9,10,16]), 5))) == [1,10,16]
    return "All tests pass."

if __name__ == '__main__':
    m = list(input("Enter the positions of the moles: "))
print(whack(m))
