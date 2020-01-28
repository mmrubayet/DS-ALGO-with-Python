def quick(lisA):
    iLength = len(lisA)
    if iLength <= 1:
        return lisA
    else:
        pivot = lisA.pop()

    iGr = []
    iLr = []

    for i in lisA:
        if i > pivot:
            iGr.append(i)
        else:
            iLr.append(i)
    return quick(iLr) + [pivot] + quick(iGr)

myList = list(map(int, input("""I can sort any array Using Bubble sort algorithm.
Enter some Integer Numbers separated by spaces.\n""").split()))

print('Given:', myList )

print("Sorted using Insertion Sort: ", quick(myList))
