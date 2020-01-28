def sel_sort(listA):
    iLength = range(0, len(listA)-1)

    for i in iLength:
        minValue = i

        for j in range(i+1, len(listA)):
            if listA[j] < listA[minValue]:
                minValue = j

        if minValue != i:
            listA[minValue], listA[i] = listA[i], listA[minValue]

    return listA

myList = list(map(int, input("""I can sort any array Using Bubble sort algorithm.
Enter some Integer Numbers separated by spaces.\n""").split()))

print(sel_sort(myList))
