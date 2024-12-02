def read_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

def keyword_filter(keyword):
    while True:
        line = (yield)
        if keyword in line:
            yield line

def to_uppercase(lines):
    for line in lines:
        yield line.upper()

def process_file(filename, keyword):
    lines = read_lines(filename)
    filtered = keyword_filter(keyword)
    next(filtered)

    for line in lines:
        try:
            filtered_line = filtered.send(line)
            if filtered_line:
                yield from to_uppercase([filtered_line])
        except StopIteration:
            break

filename = "example.txt"
keyword = "python"

for result in process_file(filename, keyword):
    print(result)



