n = int(input())
sum = sum(list(map(int,str(n))))
print('Yes' if n%sum == 0 else 'No')