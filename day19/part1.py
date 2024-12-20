from collections import deque

##### Methods

# Recursive function
def is_possible(design):
  if design in memo:
    return memo[design]

  for pattern in patterns:
    if pattern == design: return True # base case

    if design.startswith(pattern):
      i = len(pattern)
      if possible := is_possible(design[i:]):
        memo[design] = 1
        return possible

  return False

#####

file = open('input.txt', 'r')
patterns, designs = file.read().split('\n\n')
file.close()

patterns = patterns.split(', ')
designs = designs.split('\n')

memo = {}

num_possible_designs = sum(1 for design in designs if is_possible(design))
print(num_possible_designs)