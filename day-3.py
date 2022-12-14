import string
from common import parse_file

alphabet = list(string.ascii_letters)
letter_to_priority = {alphabet[i] : i+1 for i in range(len(alphabet))}
FILE_PATH = './inputs/day-3.txt'

# find shared element and return priority
def find_shared_element(line):
  compartment_1, compartment_2 = line[:len(line)//2], line[len(line)//2:]
  intersection = list(set(compartment_1) & set(compartment_2))
  print(intersection)
  return letter_to_priority[intersection[0]]
    
summ = 0
for line in parse_file(FILE_PATH):
    summ += find_shared_element(line)
print(summ)
    