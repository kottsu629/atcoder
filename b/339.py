#https://atcoder.jp/contests/abc339/tasks/abc339_b




h,w,n=map(int,input().split())

c=[[ "." for _ in range(w)]for _ in range(h)]
dh=[-1,0,1,0]
dw=[0,1,0,-1]
a,b=0,0
direction=0
for i in range(n):
  if c[a][b]==".":
    c[a][b]="#"
    direction=(direction+1)%4
  else:
    c[a][b]="."
    direction=(direction-1)%4
    
  a=(a+dh[direction])%h
  b=(b+dw[direction])%w 
for row in c:
  print("".join(row))