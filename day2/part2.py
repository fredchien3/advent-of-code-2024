file = open('input.txt', 'r')

def is_safe(report):
  # determine the initial direction for the first two levels
  # 1 for increasing, -1 for decreasing
  # unsafe if first two are the same.
  if report[0] < report[1]:
    direction = 1
  elif report[0] > report[1]:
    direction = -1
  else:
    return False

  for j in range(1, len(report)):

    left, right = report[j - 1], report[j]

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
  report_list = list(map(int, report.split(" ")))

  if is_safe(report_list):
    safe_reports += 1
  else:
    for i in range(len(report_list)):
      new_report_list = list(report_list)
      del new_report_list[i]
      if is_safe(new_report_list):
        safe_reports += 1
        break

print(safe_reports)

file.close()