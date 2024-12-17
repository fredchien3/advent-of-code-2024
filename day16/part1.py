from collections import deque, defaultdict

directions = {
  'n': (-1,  0),
  'e': ( 0,  1),
  's': ( 1,  0),
  'w': ( 0, -1)
}

### Methods
def get_neighbor_tiles(tile):
  output = []
  pos = tile['pos']
  for direction, (dy, dx) in directions.items():
    y, x = pos
    new_y, new_x = y + dy, x + dx

    if (new_y, new_x) in seen_poses: continue

    if map_string[new_y][new_x] != '#':

      weight = 1 if direction == tile['direction'] else 1001

      output.append({
        'pos': (new_y, new_x),
        'weight': weight,
        'direction': direction
      })

      seen_poses.add((new_y, new_x))

  return output

def render():
  output_map = [[' ' for _ in map_string[0]] for _ in map_string]



  for row in output_map:
    print(''.join(row))

###

file = open('input.txt', 'r')
map_string = file.read().split('\n')
file.close()


# Generate an almighty adjacency list with weights, directions, etc.
y, x = len(map_string) - 2, 1
starting_tile = {
  'pos': (y, x),
  'weight': 0,
  'direction': 'e'
}

tile_queue = deque([starting_tile])
seen_poses = set(starting_tile['pos'])
# pos: list of dicts {pos, weight, direction}
adjacency_list = defaultdict(list)

while tile_queue:
  tile = tile_queue.popleft()

  # For each neighbor, add it to the adjacency list
  neighbor_tiles = get_neighbor_tiles(tile)

  adjacency_list[tile['pos']].extend(
    neighbor_tiles
  )

  seen_poses.update(tile['pos'] for tile in neighbor_tiles)
  tile_queue.extend(neighbor_tiles)

# Run Dijkstra's algorithm
tile_queue = deque([starting_tile])
seen_poses = set(starting_tile['pos'])
distances = defaultdict(lambda: float('inf'))
distances[starting_tile['pos']] = 0

while tile_queue:
  current_tile = tile_queue.popleft()
  current_pos = current_tile['pos']

  for neighbor in adjacency_list[current_pos]:
    n_pos, n_weight = neighbor['pos'], neighbor['weight']

    if n_pos in seen_poses: continue

    new_distance = min(distances[n_pos], distances[current_pos] + n_weight)
    distances[n_pos] = new_distance

    tile_queue.append(neighbor)

  seen_poses.add(current_pos)

finish_pos = (1, len(map_string[0]) - 2)

print(distances[(1, 12)])
print(distances[finish_pos])
print(distances[(2, 13)])