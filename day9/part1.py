file = open('input.txt', 'r')

disk_map = list(map(int, file.read()))

# Unpack the disk map to see the original file blocks
file_blocks = []
id = 0
for i in range(0, len(disk_map), 2):
  for j in range(disk_map[i]):
    file_blocks.append(str(id))
  if i+1 < len(disk_map):
    for j in range(disk_map[i+1]):
      file_blocks.append('.')
  id += 1

print(file_blocks, '\n')

# Use two pointers to move file blocks
# from the end to the leftmost free space
l, r = 0, len(file_blocks) - 1

while r >= l:
  while file_blocks[l] != '.':
    l += 1
  while file_blocks[r] == '.':
    r -= 1

  file_blocks[l], file_blocks[r] = file_blocks[r], file_blocks[l]

# Looks like an off by one type error........ do it again 🤪
l -= 1
r += 1
while r > l:
  while file_blocks[l] != '.':
    l += 1
  while file_blocks[r] == '.':
    r -= 1

  file_blocks[l], file_blocks[r] = file_blocks[r], file_blocks[l]

  l += 1
  r -= 1

print(file_blocks)

checksum = 0

for i, num in enumerate(file_blocks):
  if not num == '.':
    checksum += (i * int(num))

print(checksum)

file.close()