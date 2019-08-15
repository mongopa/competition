N = int(input())
li = list("".join(sorted(input())) for _ in range(N))
dic = {}
ans = 0
for i in range(N):
  if li[i] in dic:
    ans += dic[li[i]]
    dic[li[i]] += 1
  else:
    dic[li[i]] = 1
print(ans)