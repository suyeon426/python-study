d=dict()
for _ in range(int(input())):
    book= input()
    if book in d:
        d[book] +=1
    else:   #새로 들어온 책인 경우
        d[book] =1

m= max(d.values())
candi=[]
for k, v in d.items():
    if v==m:
        candi.append(k)

candi.sort()
print(candi[0])
#print(sorted(candi)[0])
