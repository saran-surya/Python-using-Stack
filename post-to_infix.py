a=list(input())
opr,ans=["+","-","/","*","^"],[]
for i in a:
    if i not in opr:ans.append(i)
    else:
        x=ans.pop()
        ans.append(i)
        ans.append(x)
print(*ans,sep='')