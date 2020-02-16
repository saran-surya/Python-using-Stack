def rotate(a,i):
    if(a==[]): return []
    elif(i>len(a)): return a
    else:
        a.insert(i,a.pop())
        return rotate(a,i+1)

x=list(map(int,input().split()))
i=0
print(*rotate(x,i))
