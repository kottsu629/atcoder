# https://atcoder.jp/contests/abc336/tasks/abc336_b



#解法1
n = int(input())
ans = 0

for i in reversed(f"{n:08b}"):
    if i == "0":
        ans += 1
    else:
        break
print(ans)

#解法2
n = int(input())
s = f"{n:08b}"

ans = len(s) - len(s.rstrip("0"))
print(ans)