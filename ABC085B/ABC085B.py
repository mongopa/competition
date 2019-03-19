n = int(input())
li = [input() for _ in range(n)]
print(len(set(map(int,li))))