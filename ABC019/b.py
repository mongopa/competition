S = input() + '?'
cnt = 1
ans = ''
for i in range(1, len(S)):
  if S[i] == S[i - 1]:
    cnt += 1
  else:
    ans += S[i - 1] + str(cnt)
    cnt = 1
print(ans)