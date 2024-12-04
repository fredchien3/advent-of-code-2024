import re

def execute_instruction(instruction):
  numbers = instruction[4: -1].split(',')
  numbers = list(map(int, numbers))
  return numbers[0] * numbers[1]

file = open('input.txt', 'r')

content = file.read()
valid_instructions = re.findall("mul\(\d+,\d+\)", content)

results = map(execute_instruction, valid_instructions)

print(sum(results))

file.close()