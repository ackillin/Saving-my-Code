import random
x = lambda i : random.randrange(1000000)
user = int(input("Number of lottos"))
listy = []
for i in range(user):
    listy.append(random.randrange(1000000))
listy.sort()
print(listy)
winning = random.randrange(1000000)
print(f"winning number is {winning}")
if (winning in listy):
    print("You won")
else:
    print("You lost")
