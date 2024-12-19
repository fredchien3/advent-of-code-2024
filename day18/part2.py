from collections import deque

directions = {
  '<': ( 0, -1),
  '^': (-1,  0),
  '>': ( 0,  1),
  'v': ( 1,  0)
}

##### Methods

# Takes the byte that is up next in line, and drops it,
# modifying the field.
def drop_byte():
  if not byte_positions: return
  position = byte_positions.popleft()
  x, y = position
  space[y][x] = '#'
  return position

def render():
  for row in space:
    print(''.join(row))
  print('\n')

def in_bounds(pos):
  y, x = pos
  return ( y >= 0 and y < len(space) and
           x >= 0 and x < len(space[0]) )

# BFS
def get_path(start, end):
  previous = {}

  ey, ex = end
  queue = deque([start])
  seen = set()
  while queue:
    current = queue.popleft()

    if current in seen: continue

    seen.add(current)

    if current == end:
      break

    for _, delta in directions.items():
      cy, cx = current
      dy, dx = delta
      ny, nx = cy + dy, cx + dx
      next_pos = (ny, nx)

      if next_pos in seen: continue
      if not in_bounds(next_pos): continue
      if space[ny][nx] == '#': continue

      queue.append(next_pos)
      previous[next_pos] = current

  path = deque()
  current = end
  while previous.get(current):
    path.appendleft(current)
    current = previous[current]

  return path

#####

file = open('input.txt', 'r')
byte_strings = file.read().split('\n')
file.close()

byte_positions = deque([
  tuple(
    int(i) for i in byte_string.split(',')
  ) for byte_string in byte_strings
])

### Input variables
max_index = 70
num_initial_bytes_to_drop = 1024
###

size = max_index + 1
space = [['.' for _ in range(size)] for _ in range(size)]

# This isn't necessary -
# But we know that the first 1024 bytes are safe, so might as well
# save ourselves those 1024 BFS calculations.
for _ in range(num_initial_bytes_to_drop):
  drop_byte()

pos = (0, 0)
target = (max_index, max_index)

path = get_path(pos, target)
while path:
  dropped_byte = drop_byte()
  path = get_path(pos, target)
  if not path:
    print(dropped_byte)
    break

render()