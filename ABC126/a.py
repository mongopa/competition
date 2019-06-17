n, k = map(int, input().split())
s = input()
ans = []
for i in range(n):
  if i + 1 == k:
    ans.append(s[i].lower())
  else:
    ans.append(s[i])
print(''.join(ans))