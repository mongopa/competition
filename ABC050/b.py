n = int(input())
li = list(map(int, input().split()))
m = int(input())
for i in range(m):
  p, x = map(int, input().split())
  print(sum(li) - li[p - 1] + x)