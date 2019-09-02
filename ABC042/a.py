li = list(map(int, input().split()))
print('YES' if li.count(5) == 2 and li.count(7) == 1 else 'NO')