class Iterator:
    def __init__(self, start, end, step, marta):
        self.current = start
        self.end = end
        self.step = step 
        self.marta = marta

    def __iter__(self):
        return self
    
    def __next__(self):
        i=0
        while i<=self.marta:
            i+=1
            if self.current<=self.end:
                res = self.current
                self.current+=self.step
                return res   
            else:
                    raise StopIteration
            
result = Iterator(start=1, end=10, step=2, marta=2)
for i in result:
    print(i)