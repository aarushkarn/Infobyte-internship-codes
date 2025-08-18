import ctypes
class mylist:
    
    def __init__(self):
        self.size= 1
        self.n= 0
        self.a = self.createarray(self.size)
        
    def __createarray(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __resize(self,new_capacity):
        B = self.__createarray(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.a[i]
        self.A = B
    
    def append(self,item):  
        if self.n == self.size:
          self.__resize(self.size*2)
        self.a[self.n]=item
        self.n = self.n+1
          
    def pop(self,item):
        if self.n==0:
            return None
        if item < 0 or item >= self.n:
            return print("Index out of range")
        for i in range (0, self.n):
            if i == item:
                for j in range(i, self.n-1):
                    self.a[j] = self.a[j+1]
                self.n -= 1
                return
            
    def find (self,item):
        for i in range(0,self.n,++i):
            if self.a[i]== item:
                print("The iteam is:",self.a[i])
            return "item not in list"
        
l = mylist()
l.append(1)
l.append(2) 
l.append(3)
l.append(4)
l.append(5)
print(l)