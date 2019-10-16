# QuickSort
# is NOT Stable
# Worst complexity: n^2
# Average complexity: n*log(n)
# Best complexity: n*log(n)

def partition(arrayIn, low, high):
    pivot = high
    wall = low - 1

    for j in range(low, high-1):
        if arrayIn[j] < arrayIn[pivot]:
            wall += 1
            arrayIn[wall], arrayIn[j] = arrayIn[j], arrayIn[wall]
    
    #put the pivot after the wall
    arrayIn[wall+1], arrayIn[pivot] = arrayIn[pivot], arrayIn[wall+1]

    return wall + 1 #which is the position of the pivot

def quickSort(arrayIn, low, high):
    if low < high:
        pivot = partition(arrayIn, low, high) # is the midpoint dividing left and right lists

        #sort the left list
        quickSort(arrayIn, low, pivot-1)
        #sort the right list
        quickSort(arrayIn, pivot+1, high)


    


testArray = [7, 2, 1, 8, 6, 3, 5, 4]
print(str(quickSort(testArray, 0, len(testArray) -1)))
