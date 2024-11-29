class CharacterNotFoundException(Exception):
    pass

def parse_file(lines):
    grid = [[]] # Add an empty row at the beginning as to offset the index of 0, so the grid X starts at 1

    for line in lines:
        # Remove newline characters and split the line into characters
        row = list(line.strip())
        grid.append(row)

    return grid

def find_position_of_char(grid, target_char):
    # Iterate through rows and columns to find the target character
    for row_idx, row in enumerate(grid):
        if target_char in row:
            col_idx = row.index(target_char)
            return row_idx, col_idx

    return None # error handling


default_moves = {'north': False, 'south': False, 'east': False, 'west': False}
pipe_map = {
    '|': {'north': True, 'south': True, **default_moves},
    '-': {'east': True, 'west': True, **default_moves},
    'L': {'north': True, 'east': True, **default_moves},
    'J': {'north': True, 'west': True, **default_moves},
    '7': {'south': True, 'west': True, **default_moves},
    'F': {'south': True, 'east': True, **default_moves}
}

def allowed_move(current_position,proposed_position):
    return True

def calc_possible_moves(position, grid):
    allowed_moves = []

    x = position[0]
    y = position[1]

    # calculate adjacent positions
    left = tuple(x-1,y)
    right = tuple(x+1,y)
    up = tuple(x,y-1)
    down = tuple(x,y+1)

    if allowed(left):
        allowed_moves.append(left)
    if allowed(right):
        allowed_moves.append(right)
    if allowed(up):
        allowed_moves.append(up)
    if allowed(down):
        allowed_moves.append(down)

    return allowed_moves

def start(grid, start_position):
    # For the first iteration, is it significant to establish what 'S' is in place of?

    # For the start position, calculate the valid moves that can be made so we know where to go next
    allowed_moves = calc_possible_moves(start_position,grid)

    for allowed_move in allowed_moves:
        # do something
        print()

    return True

try:
    file_name = "input_test.txt"
    
    with open(file_name, 'r') as file:
        lines = file.readlines()

        # create a 2D array representing the grid
        grid = parse_file(lines)

        target_char = 'S' # start position defined by 'S'
        start_position = find_position_of_char(grid,target_char) # e.g. (96,74)

        if not start_position:
            raise CharacterNotFoundException(f"The character '{target_char}' is not found in the grid.")            
        
        print("Start position is :: " + str(start_position))

        # Now knowing where the start position is
        # we must find only loops from there
        # in order to do that, we need to understand how
        # to navigate from a given position
        results = start(grid, start_position)


except CharacterNotFoundException as e:
    print(e)
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")