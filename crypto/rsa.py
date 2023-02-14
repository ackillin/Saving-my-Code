import random,os,sys, math,cryptomath as cm, rabinMiller as rm

def convert (a):
    woo = []
    for i in a:
        for j in i:
            woo.append(int(j))
    return woo

def createKeys(keySize):
    p = rm.generateLargePrime(keySize)
    q = rm.generateLargePrime(keySize)
    #print(q)
    #Compute n, the main secret.
    n = (p) * (q)
    #print(n)
    #Compute the Least Common Multiple between the two
    t = math.lcm(p-1,q-1)
    #Compute E which is co-prime to previous (t)
    while True:
        e = random.randrange(t)
        if cm.gcd(e,t) == 1:
            #print("Hit")
            break
    #Compute d, which is the mod mult inverse of e and t
    d = cm.findModInverse(e,t)
    #print(d)
    publicKey = (n,e)
    privateKey = (n,d)
    print("Private Key",privateKey)
    print("Public Key",publicKey)
    return (publicKey,privateKey)

def encrypt(m,pubKey):
    print("Start encryption")
    t = m**pubKey[1]
    print("Step 1")
    l = t%pubKey[0]
    print(l)
    return(l)

def decrypt(msg, privKey):
    print("Start Decryption")
    t = msg **privKey[0ex]
    return(t%privKey[1])

def sanitize(listy):
    woo = []
    for i in listy:
        temp = i.replace('\n','')
        temp = temp.replace(' ','')
        if not temp.find("(") == -1:
            temp = temp.replace('(','')
            temp = temp.replace(')','')
            woo.append(tuple(temp.split(',')))
    return convert(woo)

#pubKey, privKey = createKeys(32)
file = open("keys.txt","r")
contents = file.readlines()
#file.write(f"Starting public key \n{pubKey}\n")
#file.write(f"Starting private key \n{privKey}\n")
#start = 18
#print("Keys created message is:",start)
#print(contents)
sans = sanitize(contents)
print(sans)

msg = encrypt(int(2),(sans[0],sans[1]))
#file.write(str(msg))

#demsg = decrypt(msg,(sans[2],sans[3]))
#print(demsg)
file.close()
