a=list(input())
opr,ans=["+","-","/","*","^"],[]
for i in a[::-1]:
    if i not in opr:ans.append(i)
    else:ans.append(ans.pop()+ans.pop()+i)
print(*ans)