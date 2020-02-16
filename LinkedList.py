class node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __str__(self):
        return str(self.data)

class linked(node):
    def __init__(self):
        self.head=None 
        self.tail=None 

    def insert(self,data):
        if(self.head==None):
            self.head=self.tail=node(data)
        else:
            new=node(data)
            if(self.tail.next==None):
                self.head.next=new
                self.tail.next=new
                self.tail=self.tail.next
                
    def pr(self):
        ans=[]
        c=self.head
        while(c.next):
            ans.append(c.data)
            c=c.next
        ans.append(c.data)
        return ans



    def __str__(self):
        if(self.head==self.tail):
            return "[" + str(self.head) + "]"
        else:
            c=""
            x=self.head
            while(x.next):
                c+=str(x)
                c+=","
                x=x.next
            c+=str(x)
            return "["+c+"]"

a=linked()
a.insert(1)
a.insert(2)
print(a)