# Selection sort for numbers
# is NOT Stable
# Worst complexity: n^2
# Average complexity: n^2
# Best complexity: n^2


def selectionSort(arrayIn):
    i = 0
    while i != len(arrayIn):
        low = arrayIn[i]

        for j in range(i+1, len(arrayIn)):
            cursor = arrayIn[j]
            if cursor < low:
                low = cursor
                arrayIn[j], arrayIn[i] = arrayIn[i], arrayIn[j]
        i+=1


testList = [2,3,1,5, 6,3,32,4,5,6,52,2,1]
print("before: " + str(testList))
selectionSort(testList)
print("after: " + str(testList))