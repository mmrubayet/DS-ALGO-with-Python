def quick(listA):
    iLength = len(listA)
    if iLength <= 1:
        return listA
    else:
        pivot = listA.pop()

    iGr = []
    iLr = []

    for i in listA:
        if i > pivot:
            iGr.append(i)
        else:
            iLr.append(i)
    return quick(iLr) + [pivot] + quick(iGr)

myList = list(map(int, input("""I can sort any array Using Quick sort algorithm.
Enter some Integer Numbers separated by spaces.\n""").split()))

print('Given:', myList )

print("Sorted using Quick Sort: ", quick(myList))
