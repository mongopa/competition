N, K = map(int, input().split())
li = list(map(int, input().split()))
print(len([i for i in li if i >= K]))
