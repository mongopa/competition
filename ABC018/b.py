S = input()
N = int(input())
for i in range(N):
  str, end = map(int, input().split())
  S = S[:str - 1] + S[str - 1:end][::-1] + S[end:]
print(S)