from collections import deque
from direction_map import direction_map

file = open('input.txt', 'r')

map = file.read().split('\n')

def locate_starting_pos(map):
  for i, row in enumerate(map):
    for j, ele in enumerate(row):
      if ele == '^':
        return [i, j]
  return [-1, -1]

def in_bounds(pos):
  return ( pos[0] >= 0 and pos[0] < len(map) and
           pos[1] >= 0 and pos[1] < len(map[0]) )

def get_modified_position(pos, direction):
  mod = direction_map[direction]
  new_pos = [
    pos[0] + mod[0],
    pos[1] + mod[1]
  ]
  return new_pos

def clear_ahead(pos, direction):
  ahead_pos = get_modified_position(pos, direction)
  if not in_bounds(ahead_pos):
    return True

  i, j = ahead_pos
  ahead_value = map[i][j]

  return True if (ahead_value != '#') else False

def walk_ahead(pos, direction):
  return get_modified_position(pos, direction)


pos = locate_starting_pos(map)
count = 0
directions = deque(['n', 'e', 's', 'w'])
visited = set()

while (in_bounds(pos)):
  direction = directions[0]

  if clear_ahead(pos, direction):

    if tuple(pos) not in visited:
      count += 1
      visited.add(tuple(pos))

    pos = walk_ahead(pos, direction)

  else:
    directions.rotate(-1)

print(count)

file.close()