# recursive function

def factorial(num):

    if num == 1:
        return 1

    return num * factorial(num - 1)


print(factorial(4))


# making flat list
def flattern_list(aList, result=None):

    if result is None:
        result = []

    for a in aList:
        if isinstance(a, list):
            flattern_list(a, result)
        else:
            result.append(a)

    return result


print(flattern_list([[1, 2, [3, 4]], [5, 6], 7]))
