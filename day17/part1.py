### Methods

def parse_registers(input_registers):
  registers_list = input_registers.split('\n')
  registers = {}

  for register in registers_list:
    register_list = register.split(' ')
    registers[register_list[1][0]] = int(register_list[2])

  return registers

def parse_program(input_program):
  program_list = input_program.split(' ')
  return [int(x) for x in program_list[1].split(',')]

def get_combos(registers):
  return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: registers['A'],
    5: registers['B'],
    6: registers['C'],
    7: None # will not appear in valid programs
  }

def run_instruction(opcode, operand):
  combos = get_combos(registers)

  dv_result = registers['A'] // (2 ** combos[operand])
  if opcode == 0: # adv
    registers['A'] = dv_result
    return
  if opcode == 1: # bxl
    registers['B'] = registers['B'] ^ operand
    return
  if opcode == 2: # bst
    registers['B'] = combos[operand] % 8
    return
  if opcode == 3: # jnz
    if registers['A'] > 0:
      return {'update_pointer': operand}
  if opcode == 4: # bxc
    registers['B'] = registers['B'] ^ registers['C']
  if opcode == 5: # out
    output.append(combos[operand] % 8)
    return
  if opcode == 6: # bdv
    registers['B'] = dv_result
    return
  if opcode == 7: #cdv
    registers['C'] = dv_result
    return

###

file = open('input.txt', 'r')

input_registers, input_program = file.read().split('\n\n')

file.close()

registers = parse_registers(input_registers)
program = parse_program(input_program)

output = []
i = 0
while i < len(program) - 1:
  opcode = program[i]

  if i+1 >= len(program):
    print('odd')
    break

  operand = program[i+1]

  result = run_instruction(opcode, operand)
  if result:
    i = result['update_pointer']
  else:
    i += 2

print(','.join([str(x) for x in output]))