def merge(nlist):
    print("Splitting \t",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        merge(lefthalf)
        merge(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging \t",nlist)

myList = list(map(int, input("""I can sort any array Using Merge sort algorithm.
Enter some Integer Numbers separated by spaces.\n""").split()))

print('Given: \t\t{}'.format(myList))
merge(myList)
print("Sorted using Merge Sort: {}" .format(myList))
