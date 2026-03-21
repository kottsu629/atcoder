# https://atcoder.jp/contests/abc450/tasks/abc450_b


n = int(input())
C = [[None] * (i + 1) + list(map(int, input().split())) for i in range(n - 1)]
ans = "No"
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            if C[a][b] + C[b][c] < C[a][c]:
                ans = "Yes"
print(ans)
