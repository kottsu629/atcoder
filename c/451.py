#https://atcoder.jp/contests/abc451/tasks/abc451_c


from heapq import heappop, heappush

q = int(input())
que = []

for i in range(q):
    a, h = map(int, input().split())
    if a == 1:
        heappush(que, h)
    else:
        while que and que[0] <= h:
            heappop(que)
    print(len(que))
