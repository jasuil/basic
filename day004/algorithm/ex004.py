# bubble sort


def bubbleSort(list):
    length = len(list)
    temp = 0
    for i in range(length):
        for j in range(length - 1 - i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

rList = bubbleSort([1,43,345, 436, -342, 456, 0, 4])
print(rList)
