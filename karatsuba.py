import random as rd
#This should be faster for mx+b * mx+b calculations
def kara(x1,x2,y1,y2,m):
    f = x1 * y1
    g = x2 * y2
    h = (x1+x2)*(y1+y2)
    k = h-f-g
    return (f*m^2) + k*m + g

def notkara(x1,x2,y1,y2,m):
    left = (x1 * m) + x2
    right = (y1*m) + y2
    return left * right

rad = []
for i in range(4):
    rad.append(rd.randrange(100))

print(rad)
print(kara(rad[0],rad[1],rad[2],rad[3],5))
print(notkara(rad[0],rad[1],rad[2],rad[3],5))
