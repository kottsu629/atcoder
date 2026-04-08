N = int(input())
c = [0] * (N + 1)

# x^2 + y^2 を全探索
for x in range(1, int(N**0.5) + 1):
    x2 = x * x
    # yはx+1から開始し、x^2 + y^2 <= N を満たす範囲まで
    for y in range(x + 1, int((N - x2) ** 0.5) + 1):
        c[x2 + y * y] += 1

# 1回だけ現れた数（良い整数）をリストにまとめる
ans = [i for i in range(N + 1) if c[i] == 1]

# 結果の出力
print(len(ans))
print(*ans)
