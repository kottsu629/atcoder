# https://atcoder.jp/contests/abc449/tasks/abc449_c




from collections import Counter

n, l, r = map(int, input().split())
s = input()

ans = 0
count = Counter()

# j を右端として走査
for j in range(n):
    # 新しく範囲 [j-R, j-L] に入ってくる文字 (i = j - L)
    add_idx = j - l
    if add_idx >= 0:
        count[s[add_idx]] += 1
    
    # 範囲から外れる文字 (i < j - R)
    remove_idx = j - r - 1
    if remove_idx >= 0:
        count[s[remove_idx]] -= 1
    
    # 現在の文字 s[j] と同じ文字が範囲内に何個あるか加算
    ans += count[s[j]]

print(ans)