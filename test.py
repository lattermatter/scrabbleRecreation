set1 = {1,2,3,4}
set2 = 7
print(True) if 0 or 0 in set1 else print(False)

class Test():
    def __init__(self, woah) -> None:
        self.woah = woah
        self.apple = self.woah + 5
    def get(self):
        return self.apple



obj = Test(2)
print(obj.get())
obj.woah = 5
print(obj.get())

# all object vars are not updated automatically upon changing a var

def check(a):
    b = a.copy()
    b[0] = 7
    print(a)
    
check([1,2])