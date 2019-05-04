a = input()
b = input()
for i in range(len(a)):
  if a == b:
    print('Yes')
    break
  a = a[-1]+a[:-1]
else:
  print('No')