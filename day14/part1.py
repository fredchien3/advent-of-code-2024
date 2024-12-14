import re
from collections import defaultdict
from math import prod

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

# Quadrant labels:
# 1 | 2
# -----
# 3 | 4
def count_robots(robots):
  middle_x = (width - 1)  // 2
  middle_y = (height - 1) // 2

  quadrants = defaultdict(int)

  for robot in robots:
    x, y = robot['pos']

    if y < middle_y:
      if x < middle_x:
        quadrants[1] += 1
      if x > middle_x:
        quadrants[2] += 1
    if y > middle_y:
      if x < middle_x:
        quadrants[3] += 1
      if x > middle_x:
        quadrants[4] += 1

  return quadrants

###

file = open('input.txt', 'r')

seconds = 100
width = 101
height = 103

robots = [ parse_input(row) for row in file.read().split('\n') ]

for i in range(0, seconds):
  for robot in robots:
    increment_pos(robot)

quadrants = count_robots(robots)

print(prod(quadrants.values()))

file.close()