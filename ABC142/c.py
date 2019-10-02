N = int(input())
li = list(map(int, input().split()))
ans = [0] * N
num = 1
for i in li:
    ans[i - 1] = num
    num += 1
print(*ans)