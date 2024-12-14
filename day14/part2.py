import re
from collections import defaultdict
from math import prod

directions = [
  (-1, -1),
  ( 0, -1),
  ( 1, -1),
  (-1,  0),
  ( 1,  0),
  (-1,  1),
  ( 0,  1),
  ( 1,  1),
]

### Methods

def parse_input(row):
  pos_string, vel_string = row.split(' ')

  pos_0, pos_1 = re.findall("-?\d+", pos_string)
  vel_0, vel_1 = re.findall("-?\d+", vel_string)

  pos_0, pos_1, vel_0, vel_1 = [int(x) for x in [pos_0, pos_1, vel_0, vel_1]]

  return {
    'pos': (pos_0, pos_1),
    'vel': (vel_0, vel_1)
  }

def increment_pos(robot):
  pos, vel = robot['pos'], robot['vel']
  new_pos = (pos[0] + vel[0], pos[1] + vel[1])
  robot['pos'] = wrap(new_pos)

def wrap(pos):
  x, y = pos
  if x < 0:
    x += width
  elif x > ( width - 1):
    x -= width

  if y < 0:
    y += height
  elif y > ( height - 1):
    y -= height

  return (x, y)

def is_surrounded(robot, robot_positions):
  x, y = robot['pos']

  for direction in directions:
    dx, dy = direction

    if (x + dx, y + dy) not in robot_positions:
      return False

  return True

def simulate_until_maybe_tree(robot_positions, i):
  maybe_tree = False

  while not maybe_tree:
    i += 1

    for robot in robots:
      increment_pos(robot)

    robot_positions = set(robot['pos'] for robot in robots)

    for robot in robots:
      if is_surrounded(robot, robot_positions):
        maybe_tree = True

  return (robot_positions, i)

def render(i):
  output_map = [[' ' for _ in range(0, width)] for _ in range(height)]

  for pos in robot_positions:
    x, y = pos
    output_map[y][x] = 'R'

  print('START', i)

  for row in output_map:
    print('|', ''.join(row), '|')

  print('END', i)


###

file = open('input.txt', 'r')

width = 101
height = 103

robots = [ parse_input(row) for row in file.read().split('\n') ]
robot_positions = set(robot['pos'] for robot in robots)

file.close()

i = 0
latest_input = 'ok'
while latest_input != 'stop':

  robot_positions, i = simulate_until_maybe_tree(robot_positions, i)

  render(i)

  latest_input = input("Press enter to continue, 'stop' to stop...")