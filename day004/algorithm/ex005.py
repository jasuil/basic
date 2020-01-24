# division sort

aList = [1, 43, 546, 78, -213, 345, 4]

print(sorted(aList, reverse=True))


def mergeSort(arr):

    if len(arr) == 1:
        return arr

    a = arr[:int(len(arr)/2)]
    b = arr[int(len(arr)/2):]

    a = mergeSort(a)
    b = mergeSort(b)

    c = []

    i = 0
    j = 0

    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:]
    c += b[j:]

    return c

print(mergeSort([1, 453, -45, 34, 54654, 2]))
