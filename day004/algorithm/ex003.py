# selection sort

def selectionSort(arr):

    temp = 0

    for i in range(0, len(arr)):

        for j in range(i + 1, len(arr)):

            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr


rList = selectionSort([45, -1, 45, 74, 234, 65, 8, 345, 2, 435])
print(rList)
