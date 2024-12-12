from collections import deque
from direction_map import direction_map

### Methods

def plant_at(pos):
  i, j = pos
  return farm[i][j]

def in_bounds(pos):
  return ( pos[0] >= 0 and pos[0] < len(farm) and
           pos[1] >= 0 and pos[1] < len(farm[0]) )

# Area: breadth first search to find all the in-bound,
# same plant type neighbors.
# Perimeter: Start with 4 x area. Subtract 1 for each adjacent same plant.
def appraise(pos):
  seen.add(pos)
  region = set([(pos)])

  area = 0
  current_plant = plant_at(pos)
  queue = deque((pos,))
  while queue:
    area += 1
    current_pos = queue.popleft()
    i, j = current_pos

    for d, mod in direction_map.items():
      neighbor_pos = (i + mod[0], j + mod[1])
      if not in_bounds(neighbor_pos): continue

      neighbor_plant = plant_at(neighbor_pos)

      if (neighbor_pos not in seen and
          neighbor_plant == current_plant):
        seen.add(neighbor_pos)
        region.add(neighbor_pos)
        queue.append(neighbor_pos)

  perimeter = 4 * area

  for pos in region:
    i, j = pos
    for d, mod in direction_map.items():
      neighbor_pos = (i + mod[0], j + mod[1])
      if not in_bounds(neighbor_pos): continue

      if (plant_at(neighbor_pos) == current_plant):
        perimeter -= 1

  return [area, perimeter]

###

file = open('input.txt', 'r')

farm = [list(x) for x in file.read().split('\n')]

seen = set()

total_price = 0
for i, row in enumerate(farm):
  for j, ele in enumerate(row):
    if (i, j) not in seen:
      area, perimeter = appraise((i, j))
      total_price += (area * perimeter)

print(total_price)

file.close()