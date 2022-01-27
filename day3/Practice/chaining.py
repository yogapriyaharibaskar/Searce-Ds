class HT:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]

    def get_hash(self,key):
        h=0
        for char in key:
            h+= ord(char)
        return (h%self.max)
    
    def __setitem__(self,key,val):
        h= self.get_hash(key)
        
        found=False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val))
    
    def __getitem__(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h=self.get_hash(key)
        for index , element in enumerate (self.arr[h]):
            if element[0]== key:
                del self.arr[h][index]
        
        

hashm=HT()
#hashm.add('November',24)
#print(hashm.arr)
#print(hashm.get('November'))


hashm['march 6']=120
hashm['march 6']=78
hashm['August']=5
hashm['march 17']=80
hashm['February']=17


print(hashm['march 17'])
del hashm['march 17']
print(hashm.arr)