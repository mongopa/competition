S = input()
for i in range(len(S)):
  if i % 2 == 0 and S[i] == 'L':
      print('No')
      exit()
  elif i % 2 == 1 and S[i] == 'R':
      print('No')
      exit()
print('Yes')
