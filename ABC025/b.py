N, A, B = map(int, input().split())
ans = 0
for i in range(N):
  S, D = input().split()
  D = int(D)
  if S == 'East':
    if D < A:
      ans += A
    elif B < D:
      ans += B
    else:
      ans += D
  else:
    if D < A:
      ans -= A
    elif B < D:
      ans -= B
    else:
      ans -= D

if ans < 0:
  print('West ' + str(abs(ans)))
elif 0 < ans:
  print('East ' + str(abs(ans)))
else:
  print(0)