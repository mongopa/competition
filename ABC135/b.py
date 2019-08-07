N = int(input())
li = list(map(int, input().split()))
li_sort = sorted(li)
count = 0
for i in range(N):
  if li[i] != li_sort[i]:
    count += 1
print("YES" if count <= 2 else "NO")