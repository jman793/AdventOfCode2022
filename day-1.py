# Reads the file for the next elf
def read_in_elf():
    filepath = './inputs/day-1.txt'
    calories_total = 0
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line == '\n':
                yield calories_total
                calories_total = 0
            else:
                calories_total+=int(line)
            line = fp.readline()

max_calories = 0
for calories in read_in_elf():
    max_calories = max(max_calories, calories)
print(max_calories)