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
if __name__ == "__main__":
    import timeit
    print(timeit.timeit(setup=SETUP_CODE,stmt = TEST_CODE))
    #print(timeit.timeit(stmt = TEST_CODE,number = 1000))
