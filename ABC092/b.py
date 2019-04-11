import math
n = int(input())
D, X = map(int, input().split())
li = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
  tmp = math.floor((D - 1)/li[i]) + 1
  ans += tmp

print(ans + X)