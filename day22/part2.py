from collections import deque

##### Methods

def evolve_number(number):
  multiplied = number * 64
  mixed = multiplied ^ number
  pruned = mixed % 16777216

  divided = pruned // 32
  mixed = divided ^ pruned
  pruned = mixed % 16777216

  multiplied = pruned * 2048
  mixed = multiplied ^ pruned
  pruned = mixed % 16777216

  return pruned

#####

file = open('input.txt', 'r')
file_lines = file.read().split('\n')
initial_secret_numbers = [int(line) for line in file_lines]
file.close()

changes = deque()
for num in initial_secret_numbers:
  for _ in range(10):
    digit = num % 10
    previous_num = num

    num = evolve_number(num)

    change = (num % 10) - digit

    changes.append(change)
print(changes)
