class node:
    def __init__(self,data):             #main node constructor
        self.data=data
        self.next=None 
    def __str__(self):                  # string constructor for result
        return str(self.data)
class linked(node):
    def __init__(self):
        self.head=None                  #head and tail consrtructor
        self.tail=None 
    def add(self,data):
        if(self.head==None):                         #initial check
            self.head=self.tail=node(data)
        else:
            if(self.tail.next==None): 
                self.tail.next=node(data)                  #function to insert timecom: O(1)
                self.tail=self.tail.next

    def __str__(self):
        if(self.head==self.tail): return(self.head.data)
        else:
            c=self.head
            x=""
            while(c.next):
                x+=str(c)
                c=c.next                                            #accesed directly using print() in driver program
            x+=str(c)
            return(x)
    def print(self):
        ans=[]
        c=self.head
        while(c.next):
            ans.append(c.data)                               #accesed using print(self.print) in driver program
            c=c.next
        ans.append(c.data)
        return ans
a=list(map(int,input().split()))
b=linked()
for i in a: b.add(i)
print(b)                                                     # direct access of the obkecct of the class
print("list output : ",*b.print(),sep='')                   #accessing using self.print()

