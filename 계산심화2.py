import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    A, B = input().split()
    A, B = int(A), int(B)
    print("Case","#"+str(i+1)+':',str(A),'+',str(B),'=',(A+B))