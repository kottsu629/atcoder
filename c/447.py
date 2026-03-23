# https://atcoder.jp/contests/abc447/tasks/abc447_c


# 1. 入力を受け取る
S = input().strip()
T = input().strip()

# 2. 'A' 以外の文字が一致しないなら、どうやっても無理なので -1
if S.replace("A", "") != T.replace("A", ""):
    print("-1")
else:
    # 3. A以外の文字（B, C...）をすべて「半角スペース」に置き換えてから分割する
    # これで、各区間の「Aの塊」だけが取り出せる
    import re

    s_blocks = re.split("[^A]", S)
    t_blocks = re.split("[^A]", T)

    # 4. それぞれの塊の「文字数（Aの個数）」の差を全部足す
    ans = 0
    for i in range(len(s_blocks)):
        diff = len(s_blocks[i]) - len(t_blocks[i])
        ans += abs(diff)  # 差の絶対値を足していく

    print(ans)
