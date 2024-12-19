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

# Cosmetic function.
def mark_traveled(pos):
  y, x = pos
  space[y][x] = 'O'

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

# Wait for the first n falling bytes
for _ in range(num_initial_bytes_to_drop):
  drop_byte()

render()

pos = (0, 0)
target = (max_index, max_index)
num_steps = 0
# Now take a step towards the entrance and drop a byte.
# Recalculate the path if a byte lands into the path.

path = get_path(pos, target)

while path:
  step = path.popleft()
  num_steps += 1

  mark_traveled(step)

  dropped_byte = drop_byte()

  if dropped_byte in path:
    print(dropped_byte, ' recalculating')
    path = get_path(step, target)
    continue

render()
print(num_steps)

# Addendum: Looks like I overengineered this solution.
# Part 1 just calls for dropping 1024 bytes,
# then calculating the length of the exit path.
# No further bytes needed to be dropped while traversing the path.
# Interestingly though my output is the same in both cases.