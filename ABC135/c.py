N = int(input())
enemy = list(map(int, input().split()))
heroes = list(map(int, input().split()))
ans = 0
for i in range(N):
  diff = min(enemy[i], heroes[i])
  enemy[i] -= diff
  heroes[i] -= diff
  ans += diff

  diff = min(enemy[i + 1], heroes[i])
  enemy[i + 1] -= diff
  heroes[i] -= diff
  ans += diff

print(ans)