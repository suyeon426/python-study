T=int(input())
for _ in range(T):
    stk=[]
    isVPS= True
    for ch in input():
        if ch=="(":
            stk.append(ch)
        else: #")"일 경우
            if len(stk) > 0: #스택이 비어있지 않다면
                stk.pop()
            else:
                isVPS = False
                break
    if len(stk) > 0:
        isVPS=False

    print("Yes" if isVPS else "NO")