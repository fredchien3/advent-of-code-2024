# Takes 48 passes to run the input - could improve by sorting the input first,
# and starting with the operations that contain x and y keys?

from collections import deque

file = open('input.txt', 'r')
initial_values, gate_connections = file.read().split('\n\n')
file.close()

operations = {
  'AND': '&',
  'OR': '|',
  'XOR': '^'
}

values = {}
for line in initial_values.split('\n'):
  wire, value = line.split(': ')
  values[wire] = value

gate_connections = gate_connections.split('\n')

output = deque()
seen = set()
passes = 1
while len(seen) < len(gate_connections):
  passes += 1
  for connection in gate_connections:
    wire1, gate, wire2, _, wire3 = connection.split(' ')
    operation = operations[gate]

    if wire1 not in values or wire2 not in values: continue

    result = eval(values[wire1] + operation + values[wire2])
    values[wire3] = str(result)
    seen.add(connection)

print('Number of passes:', passes)

z_keys = sorted([ key for key in values if key.startswith('z') ], reverse=True)

binary = ''.join([ values[key] for key in z_keys ])

print(int(binary, 2))