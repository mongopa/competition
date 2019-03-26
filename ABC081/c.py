import collections
n, k = map(int, input().split())
li = [int(_) for _ in input().split()]

c = sorted(collections.Counter(li).values())[:-k]
print(sum(c))