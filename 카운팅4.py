numbers = [int(input()) for _ in range(9)]
max_value = max(numbers)
max_index = numbers.index(max_value) + 1  # 인덱스는 1부터 시작하므로 +1
print(max_value)
print(max_index)