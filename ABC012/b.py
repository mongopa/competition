N = int(input())
S = N % 60
M = ((N - S) // 60) % 60
H = N // 3600
print(str(H).zfill(2) + ':' + str(M).zfill(2) + ':' + str(S).zfill(2))