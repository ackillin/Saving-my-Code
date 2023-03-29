def partition(listy,low,high):
    pivot = listy[high]
    i = low - 1
    for j in range(low,high):
        if listy[j] <=pivot:
            i = i + 1
            #Swap
            listy[i],listy[j] = listy[j],listy[i]
    listy[i+1],listy[high] = listy[high],listy[i+1]
    return i + 1
def quick_sort(listy,low = 0,high = len(listy)-1):
    if low < high:
        pi = partition(listy,low,high)
        quick_sort(listy,low,pi-1)
        quick_sort(listy,pi+1,high)
def get_rands():
    import random
    lol = []
    for i in range(1000):
        lol.append(random.randrange(2000))
    return lol
if __name__ == "__main__":
    import sys
    file = open(sys.argv[1],'r')
    print(file)
    listy = get_rands()
    quick_sort(listy,0,len(listy)-1)
    print(listy[:5])
