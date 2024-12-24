from keypads import *
import re

##### Methods

def get_map_for(keypad):
  keypad_map = {}
  for y, row in enumerate(keypad):
    for x, ele in enumerate(row):
      keypad_map[ele] = (y, x)
  return keypad_map

def diff_between(pos1, pos2):
  (y1, x1), (y2, x2) = pos1, pos2
  return (y2 - y1, x2 - x1)

# Generates the first-order moveset to reach the final door code.

# First we gather the keypad coordinates of the buttons needed for the code.
# Then we calculate the differences (deltas) between the coordinates.
# Finally, the deltas are converted to arrow key presses
# (with an 'A' press in between).

def get_numeric_moves(code):
  return get_moves(code, (3, 2), numeric_map)


# Generates the second- and third- order movesets using the directional pad(s).
# Will refactor.

def get_directional_moves(moves):
  return get_moves(moves, (0, 2), directional_map)

def get_moves(buttons, start_pos, mapping):
  deltas = []
  y, x = start_pos
  for button in buttons:
    button_position = mapping[button]
    deltas.append(diff_between((y, x), button_position))
    y, x = button_position

  directional_path = []
  for y, x in deltas:
    x_button = '<' if x < 0 else '>'
    y_button = '^' if y < 0 else 'v'

    for _ in range(abs(x)):
      directional_path.append(x_button)

    for _ in range(abs(y)):
      directional_path.append(y_button)

    directional_path.append('A') # Button press

  return directional_path


#####

file = open('input.txt', 'r')
target_door_codes = file.read().split('\n')
file.close()

numeric_map = get_map_for(numeric_keypad)
directional_map = get_map_for(directional_keypad)

output = 0

for code in target_door_codes:
  depressurized_moves = get_numeric_moves(code)
  # print(''.join(depressurized_moves))

  irradiated_moves = get_directional_moves(depressurized_moves)
  # print(''.join(irradiated_moves))

  frozen_moves = get_directional_moves(irradiated_moves)
  # print(''.join(frozen_moves))

  numeric_part = int(re.search('\d+', code).group())
  complexity = len(frozen_moves) * numeric_part
  output += complexity

  print(code, len(frozen_moves), numeric_part)

print(output)