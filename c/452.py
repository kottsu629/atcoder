#https://atcoder.jp/contests/abc452/tasks/abc452_c

import sys

def solve():
    # 入力が多いので sys.stdin.read() で一括読み込みして高速化
    input_data = sys.stdin.read().split()
    
    N = int(input_data[0])
    
    A = []
    B = []
    idx = 1
    for _ in range(N):
        A.append(int(input_data[idx]))
        B.append(int(input_data[idx+1]))
        idx += 2
        
    M = int(input_data[idx])
    idx += 1
    
    strings = input_data[idx:]
    
    # 前処理：「長さLの単語のk文字目（1-indexed）」に存在する文字の集合を保存
    # 文字列の長さは最大10なので、11x11の2次元配列を用意すれば十分
    available = [[set() for _ in range(11)] for _ in range(11)]
    
    for s in strings:
        L = len(s)
        for k in range(1, L + 1):
            available[L][k].add(s[k-1])
            
    # 各文字列が脊椎になり得るかの判定
    ans = []
    for s in strings:
        # 脊椎の長さはNでなければならない
        if len(s) != N:
            ans.append("No")
            continue
            
        is_ok = True
        for i in range(N):
            # 脊椎のi文字目（0-indexedなので s[i]）が、
            # 肋骨の条件（長さ A[i] の B[i] 文字目）として存在するかチェック
            if s[i] not in available[A[i]][B[i]]:
                is_ok = False
                break
                
        if is_ok:
            ans.append("Yes")
        else:
            ans.append("No")
            
    # 改行区切りで一括出力
    print('\n'.join(ans))

if __name__ == '__main__':
    solve()