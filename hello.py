
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
#List Comprehension example
#arr = [[0 for _ in range(K+1)] for _ in range(N+1)]
def find_stuff(N,K):
    while len(arr) < K:
        arr.append()

def count_nums(N,arr):
    count = 0
    for i in range(N):
        divis = False
        for x in range(N):
            if arr[i] % arr[x] == 0 and not divis and x !=i:
                print(arr[x],arr[i])
                count+=1
                divis = True
    return count
listy = [2,3,6]
t = 3
print(count_nums(t,listy))
