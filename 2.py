def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1

def echo_coroutine():
    print("코루틴 시작")
    while True:
        value = yield
        print(f"받은 값: {value * 2}")

gen = infinite_numbers()
co = echo_coroutine()
next(co)

while True:
    value = next(gen)
    co.send(value)