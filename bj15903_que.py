import heapq
n, m= map(int, input().split())
arr=list(map(int, input().split()))
'''arr.sort() #올림차수로 정렬

for i in range(m):
    min= arr[0] + arr[1]
    arr[0]=min
    arr[1]= min

result= sum(arr)
print(result) > 배열로 풀면 시간 초과'''

heapq.heapify(arr) #힙구조로 만들어줌
for i in range(m):
    min1= heapq.heappop(arr)
    min2=heapq.heappop(arr)

    heapq.heappush(arr, min1+ min2)
    heapq.heappush(arr, min1+ min2)

print(sum(arr))
