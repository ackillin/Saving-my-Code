def isPrime(num):
    if num ==1 or num == 2:
        return True
    i = 0
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def zeno(num):
    listy = []
    for i in range(num):
        if isPrime(i):
            listy.append(i)

    return listy

def water(num):
    primes = [2]
    for i in range(2,num):
        flag = True
        for n in primes:
            if i%n==0:
                flag = False
                break
        if flag:
            if isPrime(i):
                primes.append(i)
    return primes

if __name__ == "__main__":
    import timeit
    print("Hi Chat")
    number = int(input("What is the max number? "))
    start_time = timeit.default_timer()
    print(zeno(number))
    print(timeit.default_timer()-start_time)

    start_time = timeit.default_timer()
    print(water(number))
    print(timeit.default_timer()-start_time)
