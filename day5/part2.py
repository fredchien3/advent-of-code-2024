from collections import defaultdict
from functools import cmp_to_key

file = open('input.txt', 'r')

rules, updates = file.read().split('\n\n')

# Key = number
# Value = an array of numbers which must come after
hash = defaultdict(set)
for rule in rules.split('\n'):
  left, right = rule.split('|')
  hash[left].add(right)

def compare(num1, num2):
  return 1

def is_incorrect_update(update_string):
  update = update_string.split(',')
  seen = set()
  for number in update:
    for successor in hash[number]:
      if successor in seen:
        return True
    seen.add(number)
  return False

incorrect_updates = filter(is_incorrect_update, updates.split('\n'))

def compare(num1, num2):
  if num2 in hash[num1]:
    return -1
  else:
    return 1

sum = 0
for update_string in incorrect_updates:
  update = update_string.split(',')
  print(update)
  update.sort(key=cmp_to_key(compare))
  print(update)
  midpoint = len(update) // 2
  sum += int(update[midpoint])

print(sum)

file.close()