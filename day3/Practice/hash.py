class HT:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
#function to create hash value
    def get_hash(self,key):
        h=0
        for char in key:
            h+= ord(char)
        return (h%self.max)
# setitem is an inbuilt python operator
#this function is to set ket value pair in array
    def __setitem__(self,key,val):
        h= self.get_hash(key)
        self.arr[h]=val
#this function is to get value from array   
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]
#this function is to rempve ket value pair in array    
    def __delitem__(self,key):
        h=self.get_hash(key)
        self.arr[h]=None
        
        

hashm=HT()
#hashm.add('November',24)
#print(hashm.arr)
#print(hashm.get('November'))
hashm['November']=24
hashm['June']=18
hashm['March']=23
hashm['August']=5
hashm['February']=17

del hashm['March']
print(hashm['November'])
print(hashm.arr)