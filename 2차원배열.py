n = int(input())  # 색종이의 개수
board = [[0] * 100 for _ in range(100)]  # 100x100 크기의 좌표 평면 생성

# 색종이 붙이기
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1  # 색종이가 차지하는 부분을 1로 표시

# 총 면적 계산
total_area = sum(sum(row) for row in board)
print(total_area)