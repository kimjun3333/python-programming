# 체스 말의 기준 개수
required = [1, 1, 2, 2, 2, 8]

# 입력받은 체스 말의 현재 개수
current = list(map(int, input().split()))

# 필요한 말의 개수 계산
result = [required[i] - current[i] for i in range(6)]

# 결과 출력
print(" ".join(map(str, result)))