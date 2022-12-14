import string
from common import parse_file

alphabet = list(string.ascii_letters)
letter_to_priority = {alphabet[i] : i+1 for i in range(len(alphabet))}
FILE_PATH = './inputs/day-3.txt'

# find shared element and return priority
def find_shared_element(line1, line2, line3):
  intersection = list(set(line1) & set(line2) & set(line3))
  intersection.remove('\n')
  print(intersection)
  return letter_to_priority[intersection[0]]
    
summ = 0
lines = [line for line in parse_file(FILE_PATH)]
three_lines = []
for i in range(len(lines)):
    three_lines.append(lines[i])
    if len(three_lines) == 3:
        summ+=find_shared_element(three_lines[0], three_lines[1], three_lines[2])
        three_lines = []
print(summ)
    