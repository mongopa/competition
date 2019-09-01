ans = ''
S = input()
for i in S:
  if len(S) != 0 and i == 'B':
    ans = ans[:-1]
    continue
  elif len(S) == 0 and i == 'B':
    continue
  ans = ans + i
print(ans)