from itertools import product

file = open('input.txt', 'r')
lines = file.read().split('\n')

operators = ['+', 'x']

# Given an array of numbers, stick an operator between each number

def get_all_permutations(numbers):
  return recursive( [numbers] )

def recursive(list_of_lists):
  print(list_of_lists)
  if len(list_of_lists) == 1 and len(list_of_lists[0]) <= 1:
    return list_of_lists

  output = []
  for number_list in list_of_lists:
    recursive_case = recursive([number_list[:-1]])
    for case in recursive_case:
      for op in operators:
        output.append(case + [op] + recursive([[number_list[-1]]])[0])
  return output

# def can_possibly_be_achieved(target, string):
#   components = string.split(' ')
#   print(components)
#   layouts = []
#   layouts.extend(get_all_permutations(components))

print(get_all_permutations([1, 2, 3, 4]))

# I think I am going to start by just brute forcing -
# trying different permutations of x and + between the numbers
sum = 0

for line in lines:
  print(line)
  left, right = line.split(": ")
  if can_possibly_be_achieved(int(left), right):
    sum += int(left)

print(target)

file.close()
