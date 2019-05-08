n = int(input())
while n>=0:
  if n%4==0:
    print('Yes')
    exit()
  n -= 7
print('No')