# 바구니의 개수와 공의 개수 입력 받기
n, m = map(int, input().split())

# 바구니를 0으로 초기화
baskets = [0] * n

# M개의 작업을 수행
for _ in range(m):
    # a, b, c 입력 받기
    a, b, c = map(int, input().split())

    # a번째 바구니부터 b번째 바구니까지 c개의 공을 넣음
    for i in range(a - 1, b):
        baskets[i] = c

# 결과 출력
print(*baskets)