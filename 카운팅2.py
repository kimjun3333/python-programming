x , y = map(int, input().split())
numbers = list(map(int, input().split()))
for i in numbers:
     if i < y:
         print(i, end=' ')