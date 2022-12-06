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

calories_per_elf = [calories for calories in read_in_elf()]
calories_per_elf.sort(reverse=True)
print(sum([calories_per_elf[0], calories_per_elf[1], calories_per_elf[2]]))