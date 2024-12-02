n = int(input())

# 상단 부분
for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 하단 부분
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
