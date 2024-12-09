# Approach:
# Locate all antennas. Keep track of their locations using a dict.
from collections import defaultdict
from itertools import combinations

### Methods

def in_bounds(pos):
  return ( pos[0] >= 0 and pos[0] < len(map) and
           pos[1] >= 0 and pos[1] < len(map[0]) )

def get_antinodes_for_pair(pair): # 5, 5 and 3, 4
  pos1, pos2 = pair
  delta_i = pos1[0] - pos2[0] #  2
  delta_j = pos1[1] - pos2[1] # -2

  antinode1 = (pos1[0] + delta_i, pos1[1] + delta_j)
  antinode2 = (pos2[0] - delta_i, pos2[1] - delta_j)

  return filter(lambda x: in_bounds(x), [antinode1, antinode2])

###

file = open('input.txt', 'r')

map = file.read().split('\n')

antenna_positions = defaultdict(set)

for i, row in enumerate(map):
  for j, ele in enumerate(row):
    if ele != '.':
      # Antenna was found
      antenna_positions[ele].add((i, j))

antinode_positions = set()

for antenna, positions in antenna_positions.items():
  pos_pairs = combinations(positions, 2)
  for pair in pos_pairs:
    antinode_positions.update(get_antinodes_for_pair(pair))

print(len(antinode_positions))

file.close()