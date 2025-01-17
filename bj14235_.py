import heapq

T=int(input())
gift=[]
for i in range(T):
    a=list(map(int, input().split()))
    if a[0]==0: #아이 있음
        if gift:
            print(heapq.heappop(gift)[1])
        else: #선물 x
            print(-1)
    else:
        for i in range(1,a[0]+1):
            heapq.heappush(gift, -a[i])
