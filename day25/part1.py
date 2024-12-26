from collections import deque
from itertools import product

##### Methods

def parse(schematic):
  pin_heights = []

  for x, col in enumerate(schematic[0]):

    pin_height = -1 # Ignore the leading/trailing # row
    for y in range(len(schematic)):
      if schematic[y][x] == '#':
        pin_height += 1
    pin_heights.append(pin_height)

  return pin_heights

def fit(combination):
  lock, key = combination

  for i in range(len(lock)):
    if lock[i] + key[i] >= 6:
      return False

  return True

#####

file = open('input.txt', 'r')
schematics = file.read().split('\n\n')
file.close()

locks = []
keys = []
for schematic in schematics:
  schematic_list = schematic.split('\n')

  pin_heights = parse(schematic_list)

  if schematic.startswith('#####'):
    locks.append(pin_heights)
  else:
    keys.append(pin_heights)

print(locks)
print(keys)

num_fitting_pairs = 0

for combination in product(locks, keys):
  if fit(combination):
    num_fitting_pairs += 1

print(num_fitting_pairs)