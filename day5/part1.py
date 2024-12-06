from collections import defaultdict

file = open('input.txt', 'r')

rules, updates = file.read().split('\n\n')

# Key = number
# Value = an array of numbers which must come after
hash = defaultdict(list)
for rule in rules.split('\n'):
  left, right = rule.split('|')
  hash[left].append(right)

# Determine which updates are valid
def is_valid_update(update_string):
  update = update_string.split(',')
  seen = set()
  for number in update:
    for successor in hash[number]:
      if successor in seen:
        return False
    seen.add(number)
  return True
valid_updates = filter(is_valid_update, updates.split('\n'))

# Sum the middle numbers of the valid updates
sum = 0
for update in valid_updates:
  update = update.split(',')
  midpoint = len(update) // 2
  sum += int(update[midpoint])

print(sum)

file.close()