# Certainly not an optimal solution, but works.
# Could be improved by somehow caching the distance each point is
# from the finish, and using that to save subsequent recaculations.

from collections import deque, defaultdict

directions = [
  ( 0, -1),
  (-1,  0),
  ( 0,  1),
  ( 1,  0)
]

##### Methods

def cheatable_wall(y, x):
  if racetrack[y-1][x] == '.' and racetrack[y+1][x] == '.':
    return True
  if racetrack[y][x-1] == '.' and racetrack[y][x+1] == '.':
    return True

  return False

def run_race():
  previous = {}

  ey, ex = end
  queue = deque([start])
  seen = set()
  while queue:
    current = queue.popleft()

    if current in seen: continue

    seen.add(current)

    if current == end:
      break

    for delta in directions:
      cy, cx = current
      dy, dx = delta
      ny, nx = cy + dy, cx + dx
      next_pos = (ny, nx)

      if next_pos in seen: continue
      if racetrack[ny][nx] == '#': continue

      queue.append(next_pos)
      previous[next_pos] = current

  path = deque()
  current = end
  while previous.get(current):
    path.appendleft(current)
    current = previous[current]

  return len(path)

def try_cheat(wall):
  y, x = wall

  racetrack[y][x] = '.'

  time = run_race()

  racetrack[y][x] = '#'

  return time

#####

file = open('input.txt', 'r')
racetrack = file.read().split('\n')
file.close()
racetrack = [list(row) for row in racetrack]

# Identify start and end positions,
# as well as each (cheatable) interior racetrack wall
start = None
end = None
walls = []
for y, row in enumerate(racetrack):
  # Interior walls only
  if y == 0 or y == len(racetrack) - 1:
    continue

  for x, ele in enumerate(row):
    if x == 0 or x == len(row) - 1:
      continue

    if ele == 'S': start = (y, x)
    if ele == 'E': end = (y, x)

    if ele == '#' and cheatable_wall(y, x):
      walls.append((y, x))

initial_time = run_race()

# key: time saved
# value: number of cheats that save this amount of time
cheats = defaultdict(int)
for wall in walls:
  cheated_time = try_cheat(wall)

  if cheated_time == initial_time: continue

  time_saved = initial_time - cheated_time

  cheats[time_saved] += 1

num_cheats_that_save_at_least_100_picoseconds = sum([v for k, v in cheats.items() if k >= 100])
print(num_cheats_that_save_at_least_100_picoseconds)