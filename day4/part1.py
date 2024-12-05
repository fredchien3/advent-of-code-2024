file = open('input.txt', 'r')

rows = file.read().split('\n')

# these bounds are exclusive
left_bound = 0
upper_bound = 0
right_bound = len(rows[0]) - 1
lower_bound = len(rows) - 1

directions = [
  [ 0,  1], # right
  [ 0, -1], # left
  [-1,  0], # up
  [ 1,  0], # down
  [-1,  1], # upright
  [ 1, -1], # downleft
  [-1, -1], # upleft
  [ 1,  1] # downright
]

# Given coordinates in the input, search all eight directions
# and return the number of XMASes found.
def num_xmases(i, j):
  count = 0
  letter = rows[i][j]

  for direction in directions:
    if check_direction(i, j, direction):
        count += 1
  return count

def check_direction(i, j, direction):
  i_offset, j_offset = direction
  checked_letters = []
  for n in range(0, 4):
    new_i = i + (i_offset * n)
    new_j = j + (j_offset * n)
    if (new_i < upper_bound or new_i > lower_bound or
        new_j < left_bound  or new_j > right_bound):
      return False
    checked_letters.append(rows[new_i][new_j])
  return ''.join(checked_letters) == 'XMAS'

total_xmases = 0

for i, row in enumerate(rows):
  for j, letter in enumerate(row):
    if letter == 'X':
      total_xmases += num_xmases(i, j)

print(total_xmases)


file.close()