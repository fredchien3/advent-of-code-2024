### Methods

# Takes a number input and returns a list with the new value(s)
def process_stone(num):
  if num == 0:
    return [1]

  # Else if the number of digits is even, split the stone into two
  elif (num_digits := len(num_as_string := str(num))) % 2 == 0:
    mid_i = (num_digits // 2)
    left, right = num_as_string[:mid_i], num_as_string[mid_i:]
    return [int(left), int(right)]

  else:
    return [num * 2024]

# Mutates the stones list according to the rules
def blink(stones):
  output = []
  for num in stones:
    output.extend(process_stone(num))
  return output

###

file = open('input.txt', 'r')

stones = [int(x) for x in file.read().split(' ')]
print(stones)

for i in range(25):
  stones = blink(stones)
  print(stones)

print(len(stones))

file.close()