
def first(a):
    return lambda b : b *a
"""
lam = first(2)
#print(lam(11))
listy = []
listy.append("Hello")
listy.append("Cheese")
print("Cheese" in listy)

tupel = ("Test",5,)
print(tupel)
addd = ("add on",)
tupel += addd
print(tupel)
"""
#Sum = N
#Total Length of Arr = K
arr = [[0 for _ in range(K+1)] for _ in range(N+1)]
def find_stuff(N,K):
    while len(arr) < K:
        arr.append()
