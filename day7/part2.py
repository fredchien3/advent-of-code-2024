from itertools import product

file = open('input.txt', 'r')
lines = file.read().split('\n')

operators = ['+', '*', '||']

# A recursive function. Is passed a list of lists of numbers like [[1, 2, 3]],
# and outputs permutations by sticking the operators in the gaps between numbers.

def get_all_permutations(list_of_lists):
  if len(list_of_lists) == 1 and len(list_of_lists[0]) <= 1:
    return list_of_lists

  output = []
  for number_list in list_of_lists:
    recursive_case = get_all_permutations([number_list[:-1]])
    for case in recursive_case:
      for op in operators:
        output.append(case + [op] + get_all_permutations([[number_list[-1]]])[0])

  return output

def evaluate(formula):
  result = formula[0]

  for i in range(1, len(formula) - 1, 2):
    operator = formula[i]

    if operator == '||':
      result = int(str(result) + str(formula[i+1]))
    else:
      newformula = ''.join([str(result), formula[i], formula[i+1]])
      result = eval(newformula)

  return result

def can_possibly_be_achieved(target, string):
  components = string.split(' ')

  formulas = get_all_permutations([components])

  for formula in formulas:
    if target == evaluate(formula):
      return True

  return False

# I think I am going to start by just brute forcing -
# trying different permutations of x and + between the numbers
sum = 0

for line in lines:
  left, right = line.split(": ")
  if can_possibly_be_achieved(int(left), right):
    sum += int(left)

print(sum)

file.close()
