word = input().upper()  # 입력을 대문자로 변환
alphabet_count = {}

# 각 알파벳의 빈도 계산
for char in word:
    if char in alphabet_count:
        alphabet_count[char] += 1
    else:
        alphabet_count[char] = 1

# 가장 많이 사용된 알파벳 찾기
max_count = max(alphabet_count.values())
most_common = [k for k, v in alphabet_count.items() if v == max_count]

# 결과 출력
if len(most_common) > 1:
    print('?')
else:
    print(most_common[0])