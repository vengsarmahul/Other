#Find out Happy Number

take_data = input(str('Please check following number is Happy Number: '))

class Happy_num:
    
    def __init__(self):
        self.input = take_data
        self.lst = []
        
    def sum_of_sqr_digit(self):
        square1 = self.input 
        for digi in square1:
            self.lst.append(int(digi))
        return self.lst
    
    def sqr_looping(self,square2):
        newlst = []
        for num in square2:
            newlst.append(pow(num,2))
        total = sum(newlst)
        return total


x = Happy_num()
b = x.sum_of_sqr_digit()
c = x.sqr_looping(b)

while c != 1:
    d = []
    for num in str(c):
        d.append(int(num))
    c = x.sqr_looping(d)
    
    
if sum(b) == 1 or c == 1:
    print('Its Happy Number')
