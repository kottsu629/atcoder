#https://atcoder.jp/contests/abc341/tasks/abc341_b


n=int(input())
a=list(map(int,input().split()))

for i in range(n-1):
  s,t=map(int,input().split())
  b=a[i]//s
  a[i+1]+=b*t
print(a[n-1])