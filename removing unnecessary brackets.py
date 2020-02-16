a=list(input()) #input list
stack=[]            
i=0
flag=False
while(flag!=True):
    if(a[i]=="("):
        stack.append(i)
    elif(a[i]==")"):
        if(stack==[]):a[i]=""
        elif(a[stack[-1]]=="("):stack.pop()
    i+=1
    if(i==len(a)): flag=True
if(stack==[]):
    print(*a,sep='')
else:
    for i in stack:
        a[i]=""
    print(*a,sep='') 