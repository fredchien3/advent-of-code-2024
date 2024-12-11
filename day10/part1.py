from collections import deque
from direction_map import direction_map

### Methods

def in_bounds(pos):
  return ( pos[0] >= 0 and pos[0] < len(topo_map) and
           pos[1] >= 0 and pos[1] < len(topo_map[0]) )

# breadth first search to find all the 9s
# add all in-bound, +1 height neighbors
def score(pos):
  score = 0
  queue = deque((pos,)) # stay as a tuple!
  seen = set()

  while queue:
    current_pos = queue.popleft()
    i, j = current_pos
    current_height = topo_map[i][j]

    if current_height == 9:
      score += 1

    # check each neighbor for in-bound, +1 height
    for direction, mod in direction_map.items():
      next_pos = (i + mod[0], j + mod[1])
      k, l = next_pos

      if in_bounds(next_pos):
        next_height = topo_map[k][l]

        if (next_pos not in seen and
          next_height == current_height + 1):
          seen.add(next_pos)
          queue.append(next_pos)

  return score

###

file = open('input.txt', 'r')

input_map = file.read().split('\n')
topo_map = [list(row) for row in input_map]

trailheads = set()

for i, row in enumerate(topo_map):
  for j, ele in enumerate(row):
    topo_map[i][j] = int(ele)

    if ele == '0':
      trailheads.add((i, j))
total_score = 0

for pos in trailheads:
  total_score += score(pos)

print(total_score)

file.close()