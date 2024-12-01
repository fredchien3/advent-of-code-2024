# Read the file and process the location IDs into left and right lists
file = open('input.txt', 'r')

content = file.read().split("\n")
left = []
counter = {}

for line in content:
  first, second = line.split("   ")
  left.append(first)

  # Instead of a right array, count the occurrences of each ID
  # in the right column
  if second not in counter:
    counter[second] = 0
  counter[second] += 1

# Calculate the similarity score by multiplying the left val by its count in the right col
similarity_score = 0
for num in left:
  if num in counter:
    similarity_score += int(num) * counter[num]

print(similarity_score)

file.close()