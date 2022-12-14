
def parse_file(filepath):
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            yield line
            line = fp.readline()