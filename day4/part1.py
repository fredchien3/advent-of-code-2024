file = open('input.txt', 'r')

rows = file.read().split('\n')

# these bounds are inclusive
left_bound = 3
upper_bound = 3
right_bound = len(rows[0]) - 4
lower_bound = len(rows) - 4

# Given coordinates in the input, search all eight directions
# and return the number of XMASes found.
def num_xmases(i, j):
  count = 0
  letter = rows[i][j]

  # Check horizontally both ways
  if j <= right_bound:
    four_right = []
    for offset in range(0, 4):
      four_right.append(rows[i][j + offset])
    if ''.join(four_right) == 'XMAS':
      count += 1

  if j >= left_bound:
    four_left = []
    for offset in range(0, 4):
      four_left.append(rows[i][j - offset])
    if ''.join(four_left) == 'XMAS':
      count += 1

  # Check vertically both ways
  if i >= upper_bound:
    four_above = []
    for offset in range(0, 4):
      four_above.append(rows[i - offset][j])
    if ''.join(four_above) == 'XMAS':
      count += 1

  if i <= lower_bound:
    four_below = []
    for offset in range(0, 4):
      four_below.append(rows[i + offset][j])
    if ''.join(four_below) == 'XMAS':
      count += 1

  # Check diagonally [/] way
  if i >= upper_bound and j <= right_bound:
    four_upright = []
    for offset in range(0, 4):
      four_upright.append(rows[i - offset][j + offset])
    if ''.join(four_upright) == 'XMAS':
      count += 1

  if i <= lower_bound and j >= left_bound:
    four_downleft = []
    for offset in range(0, 4):
      four_downleft.append(rows[i + offset][j - offset])
    if ''.join(four_downleft) == 'XMAS':
      count += 1

  # Check diagonally [\] way
  if i >= upper_bound and j >= left_bound:
    four_upleft = []
    for offset in range(0, 4):
      four_upleft.append(rows[i - offset][j - offset])
    if ''.join(four_upleft) == 'XMAS':
      count += 1

  if i <= lower_bound and j <= right_bound:
    four_downright = []
    for offset in range(0, 4):
      four_downright.append(rows[i + offset][j + offset])
    if ''.join(four_downright) == 'XMAS':
      count += 1

  return count


total_xmases = 0

for i, row in enumerate(rows):
  for j, letter in enumerate(row):
    if letter == 'X':
      total_xmases += num_xmases(i, j)

print(total_xmases)


file.close()