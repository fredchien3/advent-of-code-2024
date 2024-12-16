# Trying out classes and inheritance.

from classes import Robot, Box, Wall

directions = {
  '<': ( 0, -1),
  '^': (-1,  0),
  '>': ( 0,  1),
  'v': ( 1,  0)
}

### Methods
def render():
  output_map = [[' ' for _ in warehouse[0]] for _ in warehouse]

  for iterable in all_pieces:
    for piece in iterable:
      y, x = piece.pos
      output_map[y][x] = str(piece)

  for row in output_map:
    print(''.join(row))

# A recursive function.
# Moves the piece and any ahead pieces in the same direction, if possible,
# stopping if a wall is encountered.
def move_piece(current_piece, delta):
  # Walls cannot be moved.
  if (isinstance(current_piece, Wall)):
    return False

  y, x = current_piece.pos
  dy, dx = delta
  neighbor_pos = (y + dy, x + dx)

  # Check for neighbor.
  for iterable in all_pieces:
    for neighbor in iterable:
      if neighbor.pos == (neighbor_pos):
        # If there is one, try to move it. If you can, then move current piece too.
        if move_piece(neighbor, delta):
          current_piece.move(delta)
          return True
        else:
          return False

  # No neighbor. Just move the piece and return True.
  current_piece.move(delta)
  return True

###

file = open('input.txt', 'r')
map_string, moves_string = file.read().split('\n\n')
file.close()

warehouse = map_string.split('\n')

# Instantiate an object for each item in the input
robot = None
boxes = set()
walls = set()
for y, row in enumerate(warehouse):
  for x, letter in enumerate(row):
    if letter == 'O':
      boxes.add(Box((y, x)))

    elif letter == '@':
      robot = Robot((y, x))

    elif letter == '#':
      walls.add(Wall((y, x)))

all_pieces = [[robot], boxes, walls]

render()

for letter in moves_string:
  if letter == '\n': continue
  # latest_input = input("Press enter to continue")
  move_piece(robot, directions[letter])
  # render()

render()

total_gps_coordinates = sum([box.get_score() for box in boxes])
print(total_gps_coordinates)