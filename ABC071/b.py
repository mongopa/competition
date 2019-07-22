s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(alpha)):
  if alpha[i] not in s:
    print(alpha[i])
    exit()
print('None')
