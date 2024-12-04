import re

def execute_instruction(instruction):
  numbers = instruction[4: -1].split(',')
  numbers = list(map(int, numbers))
  return numbers[0] * numbers[1]

file = open('input.txt', 'r')

content = file.read()

do_dont_strings = content.split("do()")
do_strings = map(lambda string: string.split("don't()")[0], do_dont_strings)

valid_instructions = []
for do_string in do_strings:
  valid_instructions.extend(re.findall("mul\(\d+,\d+\)", do_string))

results = list(map(execute_instruction, valid_instructions))

print(sum(results))

file.close()