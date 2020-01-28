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


def binarySearch(listA, item):
    iBegin = 0
    iEnd = len(listA) - 1

    while iBegin <= iEnd:
        mid = iBegin + (iEnd - iBegin) // 2
        midValue = listA[mid]
        if midValue == item:
            return mid

        elif item < midValue:
            iEnd = mid - 1

        else:
            iBegin = mid + 1

    return None

myList = list(map(int, input("""I can find position of any number from a Sorted
array Using quick sort and binary search algorithm.\n
Enter some Integer Numbers separated by spaces.\n\n""").split()))

print('\nGiven:', myList )

myList = quick(myList)
print("Sorted using quick Sort: ", myList)

fItem = int(input("\nNow, enter the number to find Position: "))
print(f"Position of {fItem} is: ", binarySearch(myList, fItem))
