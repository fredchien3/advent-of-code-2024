# attempt at writing a non-brute force algo
# giving up. will brute

import llist
from llist import dllist,dllistnode

file = open('input.txt', 'r')

def report_is_safe(report_list, direction, failed_once=0):
  if not direction:
    if report_list.first.value < report_list.first.next.value:
      direction = 1
    elif report_list.first.value > report_list.first.next.value:
      direction = -1
    else:
      return False

  current = report_list.first
  index = 0
  failures = 0
  while current:
    if not current.next:
      return True

    # This is the first failure
    if not levels_are_safe(direction, current.value, current.next.value):
      if failed_once > 0:
        return False
      # Try removing self
      remove_self = dllist(report_list)
      remove_self.remove(remove_self.nodeat(index))
      print(remove_self, report_is_safe(remove_self, direction, 1))
      # return report_is_safe(remove_self, 1) or report_is_safe(remove_next, 1)

      # Try removing next, if possible
      remove_next = dllist(report_list)
      remove_next.remove(remove_next.nodeat(index + 1))
      print(remove_next, report_is_safe(remove_next, 1))
      print(report_is_safe(remove_self, direction, 1) or report_is_safe(remove_next, direction, 1))
      return report_is_safe(remove_self, direction, 1) or report_is_safe(remove_next, direction, 1)
    else:
      current = current.next
      index += 1


def levels_are_safe(direction, left, right):
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
  report = list(map(int, report.split(" ")))
  report_list = dllist(report)

  # Establish the direction
  # If first and second are same, pop first and try again
  # If unable a second time, fail
  if report[0] < report[1]:
    direction = 1
  elif report[0] > report[1]:
    direction = -1
  else:
    report_list.remove(report_list.first)
    if report_is_safe(report_list, 0, 1):
      safe_reports += 1

  if report_is_safe(report_list, direction):
    safe_reports += 1

print(safe_reports)

file.close()