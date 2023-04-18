#print("Hello!") if b < b else print("Failed")
SETUP_CODE = """
def recurv(stringy):
    x = y = 0
    while "pr" in stringy or "rp" in stringy:
        while "pr" in stringy:
            x+=1
            stringy = stringy.split("pr",1)
            stringy = stringy[0]+stringy[-1]
        while "rp" in stringy:
            y+=1
            stringy = stringy.split("rp",1)
            stringy = stringy[0] + stringy[-1]
    return x,y
def solv(X,Y,S):
    tup = recurv(S)
    return(X * tup[0] + Y * tup[1])
"""
TEST_CODE = """
solv(5,4,"abppprrr")
solv(6,8,"rprrprri")
"""
SETUP_CODE_TWO = """
def countnums(N,arr):
    count = 0
    for i in range(N):
        for x in range(N):
            if i!=x and arr[i] % arr[x] == 0:
                count+=1
                break
    return count
"""
#Chatgpt's "attempt"
SETUP_CODE_FOUR = """
def countnums(N,arr):
    count = 0
    unique_arr = set(arr)
    for i in range(N):
        if any(arr[i] % x == 0 for x in unique_arr if x != arr[i]):
            count+=1
    return count
"""
#My best attempt at optimization from what I know
SETUP_CODE_THREE = """
def countnums(N,arr):
    count = 0
    for i in range(N):
        listy = arr.copy()
        listy.pop(i)
        for x in listy:
            if arr[i] % x == 0:
                count+=1
                break
    return count
"""
def countnums(N,arr,**cool):
    primers = [True] * (N+1)
    dicty = {}
    arr.sort()
    print(type(dicty))
    
    for x in range(N):
        dicty.update({arr[x]:primers[x]})
    dicty[0]=dicty[1] = False
    for i in range(2,N):
        if dicty[i]:
            for j in range(i*2,N,i):
                print(j%i)
                if j % i == 0:
                    dicty[j] = False
    return [x for x in range(2,N) if dicty[x]]

#Correct answer
SETUP_CODE_FIVE = """
def countnums(N,arr):
    freq = {}
    uniq = set()
    maximum = 0

    for i in range(N):
        freq[arr[i]] = freq.get(arr[i],0)
        uniq.add(arr[i])
        maximum = max(maximum,arr[i])

    special = set()
    for z in uniq:
        for i in range(2*z,maximum+1,z):
            if i in uniq:
                special.add(i)

    ans = 0
    for x in freq.items():
        if x[1] > 1:
            ans+= x[1]
        elif x[0] in special:
            ans+=1
    return ans
"""

def rands(N):
    import random
    return [random.randrange(10) for _ in range(N)]

if __name__ == "__main__":
    import timeit
    #print(timeit.timeit(setup=SETUP_CODE,stmt = TEST_CODE))
    #print(timeit.timeit(stmt = TEST_CODE,number = 1000))
    N = 10
    arr = rands(N)
    #print(timeit.timeit(setup = SETUP_CODE_TWO,stmt = f'countnums({N},{arr})'))
    #print(timeit.timeit(setup=SETUP_CODE_THREE,stmt=f'countnums({N},{arr})'))
    #print(timeit.timeit(setup=SETUP_CODE_FOUR,stmt=f'countnums({N},{arr})'))
    #print(timeit.timeit(setup=SETUP_CODE_FIVE,stmt=f'countnums({N},{arr})'))
    print(arr)
    print(countnums(N,arr))
