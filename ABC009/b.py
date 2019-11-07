N = int(input())
li = [int(input()) for _ in range(N)]
print(sorted(list(set(li)))[-2])