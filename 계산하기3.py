while True:
    a, b = map(int, input().split())

    # 종료 조건
    if a == 0 and b == 0:
        break

    # 두 수의 합 출력
    print(a + b)