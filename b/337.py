# https://atcoder.jp/contests/abc337/tasks/abc337_b

s = input()

if "".join(sorted(s)) == s:
    print("Yes")
else:
    print("No")
