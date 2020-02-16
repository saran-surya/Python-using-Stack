class stack():
    def __init__(self):
        self._basemem=[]
    def push(self,data):
        self._basemem.append(data)
    def pop(self):
        if(self._basemem==[]): return 0
        else: del(self._basemem[-1])
    def __str__(self):
        return self._basemem.__str__()
a=stack()
a.push(1)
a.push(2)
a.pop()
b=stack()
b.push("a")
print(a,stack())
print(b,stack())