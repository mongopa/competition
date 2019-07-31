S = input()
X = 0
for i in range(len(S)):
  X += int(S[i])
print(X)
if int(S) % X == 0:
  print('Yes')
else:
  print('No')
