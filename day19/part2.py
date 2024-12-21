from collections import deque

##### Methods

# Recursive function
def num_arrangements(design):
  arrangements = 0

  if design in memo:
    return memo[design]

  for pattern in patterns:
    if pattern == design:
      arrangements += 1
      continue

    if design.startswith(pattern):
      i = len(pattern)
      arrangements += num_arrangements(design[i:])

  memo[design] = arrangements
  return arrangements

#####

file = open('input.txt', 'r')
patterns, designs = file.read().split('\n\n')
file.close()

patterns = patterns.split(', ')
designs = designs.split('\n')

memo = {}

total_arrangements = 0
for design in designs:
  total_arrangements += num_arrangements(design)

print(total_arrangements)