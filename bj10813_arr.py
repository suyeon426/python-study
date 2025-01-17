N, M= map(int, input(). split())
arr=[i for i in range(1,N+1)]
temp=0

for x in range(M):
    i,j= map(int, input().split())
    temp=arr[i-1]
    arr[i-1]= arr[j-1]
    arr[j-1]= temp

#print(arr) > 리스트로 출력
for x in range(N):
    print(arr[x], end= " ") # 리스트 요소 공백으로 구분해 출력



