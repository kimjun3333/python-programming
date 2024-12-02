def infinite_numbers():
    num = 0
    while num < 11:
        yield num
        num += 1
gen = infinite_numbers()
for n in gen:
    print(n)