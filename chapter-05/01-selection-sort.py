def selectionSort(array):
    for i in range(len(array)-1):
        lowestNumberIndex = i
        for j in range(i+1, len(array)-1):
            if array[j] < array[lowestNumberIndex]:
                lowestNumberIndex = j
        if(lowestNumberIndex != array[i]):
            array[i], array[lowestNumberIndex] = array[lowestNumberIndex], array[i]
    return array

print(selectionSort([1,3,6,4,8,9]))