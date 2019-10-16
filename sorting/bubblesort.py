# Bubble Sort
# Is Stable
# Worst complexity: n^2
# Average complexity: n^2
# Best complexity: n
# Space complexity: 1


def bubbleSort(arrayIn):
    swapFlag = False
    firstPass = True
    while swapFlag is True or firstPass:
        #reset the flag
        swapFlag = False
        #loop through entire list
        for rIndex in range(1,len(arrayIn)):
            lIndex = rIndex - 1
            if arrayIn[lIndex] > arrayIn[rIndex]:
                arrayIn[lIndex], arrayIn[rIndex] = arrayIn[rIndex], arrayIn[lIndex]
                swapFlag = True
        firstPass = False
    return arrayIn




testArray = [11, 28, 8, 15, 50, 20, 90]
print(str(bubbleSort(testArray)))
