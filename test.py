import hashlib, timeit, random
hash = lambda a : hashlib.md5(a).digest()

rand = lambda a: random.randrange(a)
def createList(n):
    listy = []
    for i in range(n):
        listy.append(rand(n))
    return listy
def crack(goal,curr = hash(b'hash')):
    if goal == curr:
        return True
    for i in range(900000):
        curr = hash(curr)
        if goal == curr:
            print("Success")
            return True
    print("Loop Done",curr)
    #crack(goal,curr)

list_1 = createList(10)
sum = 0
print(list_1)
for i in range(len(list_1)):
    sum += list_1[i]
    sum += list_1[(i+1)%len(list_1)]
    #print(sum)
    sum = 0

user = (b'Hello')
print(hash(user))
print(user)
print(crack(user))
print(len(user))
print("Start",crack(user,b'Hello'))

stri = "hi hi hi exit"
out = f"{stri[-4:-1]}{stri[-1]}"
print(out)
print (out == "exit")
