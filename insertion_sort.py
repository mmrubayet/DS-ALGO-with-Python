def insertion(listA):
    iLength = range(1, len(listA))
    for i in iLength:
        pos = listA[i]

        while listA[i-1] > pos and i>0:
            listA[i], listA[i-1] = listA[i-1], listA[i]
            i = i - 1

    return listA

myList = list(map(int, input("""I can sort any array Using Bubble sort algorithm.
Enter some Integer Numbers separated by spaces.\n""").split()))

print('Given:', myList )

print("Sorted using Insertion Sort: ", insertion(myList))
