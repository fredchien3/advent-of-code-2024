from collections import Counter

file = open('input.txt', 'r')

rows = file.read().split('\n')

# these bounds are exclusive
left_bound = 0
upper_bound = 0
right_bound = len(rows[0]) - 1
lower_bound = len(rows) - 1

fore_directions = [ # [/]
  [-1,  1], # upright
  [ 1, -1], # downleft
]

back_directions = [ # [\]
  [-1, -1], # upleft
  [ 1,  1] # downright
]

def valid_x_mas(i, j):
  count = 0
  letter = rows[i][j]

  fore_corners, back_corners = [], []
  for direction in fore_directions:
    populate_corners(i, j, direction, fore_corners)
  if sorted(fore_corners) != ['M', 'S']:
    return False

  for direction in back_directions:
    populate_corners(i, j, direction, back_corners)
  if sorted(back_corners) != ['M', 'S']:
    return False

  return True

def populate_corners(i, j, direction, result):
  i_offset, j_offset = direction
  new_i = i + i_offset
  new_j = j + j_offset

  if (new_i < upper_bound or new_i > lower_bound or
      new_j < left_bound  or new_j > right_bound):
    return

  result.append(rows[new_i][new_j])

total_x_mases = 0

for i, row in enumerate(rows):
  for j, letter in enumerate(row):
    if letter == 'A' and valid_x_mas(i, j):
      total_x_mases += 1

print(total_x_mases)


file.close()