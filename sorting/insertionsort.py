
# Insertion sort for numbers
# IS Stable
# Worst complexity: n^2
# Average complexity: n^2
# Best complexity: n
# Space complexity: 1

def insertionSort(arrayIn):
    for marker in range(1, len(arrayIn)):
        i = marker
        j = i - 1
        while j >= 0:
            leftval = arrayIn[j]
            rightval = arrayIn[i]
            if arrayIn[i] < arrayIn[j]:
                arrayIn[i], arrayIn[j] = arrayIn[j], arrayIn[i]
                j -= 1
                i -= 1
            else:
                break


testList = [2,3,1,5, 6,3,32,4,5,6,52,2,1]
print("before: " + str(testList))
insertionSort(testList)
print("after: " + str(testList))