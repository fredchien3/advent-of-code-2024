import re
from fractions import Fraction as F

### Methods

def calculate_tokens(machine):
  machine = machine.split('\n')

  a1, a2 = re.findall("\d+", machine[0])
  b1, b2 = re.findall("\d+", machine[1])
  t1, t2 = re.findall("\d+", machine[2])

  a1, a2, b1, b2, t1, t2 = [int(x) for x in [a1, a2, b1, b2, t1, t2]]
  t1 += 10000000000000
  t2 += 10000000000000

  fish = (a1 * b2) - (a2 * b1)

  num_a = (F(b2, fish) * t1) - (F(b1, fish) * t2)
  num_b = (F(a1, fish) * t2) - (F(a2, fish) * t1)

  if int(num_a) != num_a or int(num_b) != num_b:
    return 0

  return (3*num_a) + num_b

###

file = open('input.txt', 'r')

claw_machines = file.read().split('\n\n')

tokens_needed = sum(calculate_tokens(machine) for machine in claw_machines)
print(tokens_needed)

file.close()