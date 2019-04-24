n = int(input())
s = input()
ans = 0
for i in range(n):
  tmp = len(set(s[:i]) & set(s[i:]))
  if ans < tmp:
    ans = tmp

print(ans)