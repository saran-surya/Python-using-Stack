a=list(input())
opr,ans=["+","-","/","*","^"],[]
for i in a:
    if i not in opr:ans.append(i)
    else:
        tem=i+ans.pop(-2)+ans.pop()
        ans.append(tem)
print(*ans)