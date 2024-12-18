from collections import deque, defaultdict
from classes import Position

directions = {
  'n': (-1,  0),
  'e': ( 0,  1),
  's': ( 1,  0),
  'w': ( 0, -1)
}

opposites = {
  'n': 's',
  'e': 'w',
  's': 'n',
  'w': 'e'
}

### Methods
def get_rotations(position):
  output = []
  weight = None

  for direction in directions:

    if position.direction == direction:
      continue
    elif position.direction == opposites[direction]:
      weight = 2000
    else:
      weight = 1000

    output.append(Position(position.pos, direction, weight))

  return output

def get_forward_neighbor(position):
  output = []

  y, x = position.pos
  dy, dx = directions[position.direction]
  new_y, new_x = (y + dy, x + dx)

  if map_string[new_y][new_x] == '#':
    return []

  output.append(Position((new_y, new_x), position.direction, 1))

  return output

# def render():
#   output_map = [[' ' for _ in map_string[0]] for _ in map_string]

#   for row in output_map:
#     print(''.join(row))

###

file = open('input.txt', 'r')
map_string = file.read().split('\n')
file.close()

# Generate an almighty adjacency list.
y, x = len(map_string) - 2, 1

start_position = Position((y, x), 'e', 0)
position_queue = deque([start_position])
seen_ids = set(start_position.id)

# adjacency_list[Position.id] => [Position, Position, ...]
adjacency_list = defaultdict(list)

while position_queue:
  position = position_queue.popleft()

  if position.id in seen_ids: continue

  # Add every same-spot rotation to the adjacency list.
  # This is because from any tile, a rotation is a valid move.
  rotations = get_rotations(position)
  adjacency_list[position.id].extend(rotations)

  # For each neighbor, add it to the adjacency list
  forward_neighbors = get_forward_neighbor(position)
  adjacency_list[position.id].extend(forward_neighbors)

  # Now continue the BFS traversal with each of the rotations and neighbors.
  position_queue.extend(adjacency_list[position.id])

  seen_ids.add(position.id)

# Dijkstra's algorithm
# We will use seen_ids as the set of unvisited nodes.
distances = defaultdict(lambda: float('inf'))
distances[start_position.id] = 0

fy, fx = (1, len(map_string[0]) - 2)

current_position_id = start_position.id

# Could add a condition to exit early when the target is reached
while seen_ids:

  for adjacency in adjacency_list[current_position_id]:
    if adjacency.id not in seen_ids: continue

    previous_shortest = distances[adjacency.id]
    maybe_shorter = distances[current_position_id] + adjacency.weight

    distances[adjacency.id] = min(previous_shortest, maybe_shorter)

  seen_ids.remove(current_position_id)
  if not seen_ids: break

  # I know this lookup is very very suboptimal,
  # it's almost midnight and I just want to get it working right now
  current_position_id = min(seen_ids, key = lambda k: distances[k])

fy, fx = (1, len(map_string[0]) - 2)

print(distances[fy, fx, 'n'])
print(distances[fy, fx, 'e'])