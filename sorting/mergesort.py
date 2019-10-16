# Merge Sort for numbers
# IS Stable
# Worst complexity: n*log(n)
# Average complexity: n*log(n)
# Best complexity: n*log(n)
# Space complexity: n

#given two lists that are already sorted
def merge(leftList, rightList):
    #create a temp list
    mergedList = []

    #while both lists have values, compare their first elements and append
    while leftList and rightList:
        if leftList[0] < rightList[0]:
            mergedList.append(leftList.pop(0))
        else:
            mergedList.append(rightList.pop(0))

    #if right is empty, append rest of left
    while leftList:
        mergedList.append(leftList.pop(0))
    #if left is empty, append rest of right
    while rightList:
        mergedList.append(rightList.pop(0))

    #return one merged list
    return mergedList

# recursively divide list down to size 1
def mergeSort(arrayIn):
    if len(arrayIn) == 1:
        return arrayIn
    
    mid = len(arrayIn)// 2
    leftList = arrayIn[:mid]
    rightList = arrayIn[mid:]
    
    leftList = mergeSort(leftList)
    rightList = mergeSort(rightList)
    
    return merge(leftList, rightList)


testArray = [11, 28, 8, 15, 50, 20, 90]

print(str(mergeSort(testArray)))

