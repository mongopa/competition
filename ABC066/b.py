s = input()
L = len(s)
for i in range(L):
  s = s[:L - 1]
  L = len(s)
  if L % 2 == 0:
    if s[:L // 2] == s[L // 2:]:
      print(L)
      exit()