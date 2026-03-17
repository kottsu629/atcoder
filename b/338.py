# https://atcoder.jp/contests/abc338/tasks/abc338_b


#items()で辞書をタプルのリストに変換。
#lambda関数で、タプルの2番目の要素を基準に降順、同数の場合は1番目の要素を基準に昇順でソート。


from collections import Counter

s = input()
count = Counter(s)

ans = sorted(count.items(), key=lambda x: (-x[1], x[0])) 

print(ans[0][0])