n = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
ans = 0
for i in range(n):
  comp = sum(li1[:i+1]) + sum(li2[i:])
  if ans < comp:
    ans = comp
print(ans)