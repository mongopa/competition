li = [list(map(int, input().split())) for _ in range(3)]
if li[0][0]- li[0][1] == li[1][0]- li[1][1] and li[1][0]- li[1][1] == li[2][0]- li[2][1]:
  if li[0][1]- li[0][2] == li[1][1]- li[1][2] and li[1][1]- li[1][2] == li[2][1]- li[2][2]:
    print('Yes')
  else:
    print('No')
else:
  print('No')