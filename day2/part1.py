file = open('input.txt', 'r')

def is_safe(report):
  # determine the initial direction for the first two levels
  # 1 for increasing, -1 for decreasing
  direction = 1 if int(report[0]) < int(report[1]) else -1

  for j in range(1, len(report)):

    left, right = int(report[j - 1]), int(report[j])

    # check that direction is correct
    if direction == 1 and left > right:
      return False
    elif direction == -1 and left < right:
      return False

    # check that they difference is within allowed range
    difference = abs(left - right)
    if difference < 1 or difference > 3:
      return False

  return True


reports = file.read().split("\n")

safe_reports = 0

for report in reports:
  if is_safe(report.split(" ")):
    safe_reports += 1

print(safe_reports)

file.close()