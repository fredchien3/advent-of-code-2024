from collections import deque
from direction_map import direction_map

### Methods

def in_bounds(pos):
  return ( pos[0] >= 0 and pos[0] < len(topo_map) and
           pos[1] >= 0 and pos[1] < len(topo_map[0]) )

# breadth first search to find all the 9s
def score(pos):
  score = 0
  current_height = 0
  queue = deque((pos,)) # stay as a tuple!
  seen = set()
  while queue:
    current_pos = queue.popleft()
    seen.add(current_pos)
    for direction, mod in direction_map.items():
      i, j = [current_pos[0] + mod[0], current_pos[1] + mod[1]]

      if in_bounds((i, j)) and (i, j) not in seen:
        next_height = topo_map[i][j]
        # print(next_height)
        if next_height == current_height + 1:
          queue.append((i, j))
          current_height += 1
        if next_height == 9:
          score += 1

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