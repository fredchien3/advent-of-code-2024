from collections import deque

directions = {
  '<': ( 0, -1),
  '^': (-1,  0),
  '>': ( 0,  1),
  'v': ( 1,  0)
}

### Methods
def drop_byte(position):
  x, y = position
  space[y][x] = '#'

def render():
  print('\n')
  for row in space:
    print(''.join(row))

def in_bounds(pos):
  y, x = pos
  return ( y >= 0 and y < len(space) and
           x >= 0 and x < len(space[0]) )

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

###

file = open('input.txt', 'r')

byte_strings = file.read().split('\n')

file.close()

byte_positions = [
  tuple(
    int(i) for i in byte_string.split(',')
  ) for byte_string in byte_strings
]


max_index = 6
size = max_index + 1
space = [['.' for _ in range(size)] for _ in range(size)]

# Wait for the first 12 falling bytes
for position in byte_positions[:12]:
  drop_byte(position)

render()
# Wait one more - this simulates avoiding walking directly under a falling byte
# drop_byte(byte_positions[13])

# Now take a step towards the entrance and drop a byte.
# Recalculate the path if a byte lands into it.
pos = (0, 0)
target = (max_index, max_index)
path = get_path(pos, target)
