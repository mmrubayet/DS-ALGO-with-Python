def bubble(listA):
    iLength = len(listA) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, iLength):
            if listA[i] > listA[i+1]:
                sorted = False
                listA[i], listA[i+1] = listA[i+1], listA[i]
    return listA

myList = list(map(int, input("""I can sort any array Using Bubble sort algorithm.
Enter some Integer Numbers separated by spaces.\n""").split()))

print('Given: {}'.format(myList))
print("Sorted using Bubble Sort: {}" .format(bubble(myList)))
