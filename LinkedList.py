class node(object):
    def __init__(self,data):      # Node Constructor
        self.data=data
        self.next=None

    def __str__(self):           #stringifying constructor (returns a data of head or tail)
        return str(self.data)

class linked(node):
    def __init__(self):          # constructor for head and tail
        self.head=None 
        self.tail=None 

    def insert(self,data):                      #function to insert values O(1)
        if(self.head==None):
            self.head=self.tail=node(data)
        else:
            new=node(data)                                                    
            if(self.tail.next==None):
                self.tail.next=new
                self.tail=self.tail.next
            
    '''            
    def pr(self):
        ans=[]
        c=self.head
        while(c.next):
            ans.append(c.data)                         #alternate function to print(values)  O(n)
            c=c.next
        ans.append(c.data)
        return ans
    '''


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

#Driver Function

a=linked()
t=list(map(int,input().split()))   #input for a list
for i in t: a.insert(i)
print(a)                           #printing the list using the constructor __str__ in linked() 