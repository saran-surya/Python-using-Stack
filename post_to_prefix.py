a=list(input())
opr,ans=["+","-","/","*","^"],[]
for i in a:
    if i not in opr:ans.append(i)
    else:ans.append(i+ans.pop(-2)+ans.pop())
print(*ans)