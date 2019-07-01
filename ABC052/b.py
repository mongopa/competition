n = int(input())
s = input()
ans, tmp = 0, 0
for i in range(len(s)):
  if s[i] == 'I':
    tmp += 1
    if tmp > ans:
      ans = tmp
  else:
    tmp -= 1
print(ans)