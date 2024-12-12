# Feeble attempt at memoization didn't work, ran into a segmentation fault. Will try again some other time

### Methods

# Takes a number input and returns a list with the new value(s)
def process_stone(num, memo):
  if num in memo:
    return memo[num]

  elif num == 0:
    return (1,)

  # Else if the number of digits is even, split the stone into two
  elif (num_digits := len(num_as_string := str(num))) % 2 == 0:
    mid_i = (num_digits // 2)
    left, right = num_as_string[:mid_i], num_as_string[mid_i:]

    memo[num] = (int(left), int(right))

  else:
    memo[num] = (num * 2024,)

  return memo[num]

# Mutates the stones list according to the rules
def blink(stones, memo):
  output = []
  for num in stones:
    output.extend(process_stone(num, memo))
  return output

###

file = open('input.txt', 'r')

stones = [int(x) for x in file.read().split(' ')]
print(stones)

memo = {}

for i in range(75):
  stones = blink(stones, memo)

print(stones)

print(len(stones))

file.close()