# Read the file and process the location IDs into left and right lists
file = open('input.txt', 'r')

content = file.read().split("\n")
left = []
right = []

for line in content:
  line_list = line.split("   ")
  left.append(line_list[0])
  right.append(line_list[1])

# Sort both lists
left.sort()
right.sort()

# Tally up the distances for each pair of location IDs
total_distance = 0
for i in range(len(left)):
  diff = int(left[i]) - int(right[i])
  total_distance += abs(diff)

print(total_distance)

file.close()