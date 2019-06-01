#module

def userInput(listx, num):
    print("input number of integer ", num)

    for i in range(num):
        s = input("integer input: ")
        listx.append(int(s))


def userOutput(listx, num):
    for i in range(num):
        print("{}th integer is ==> {}".format(i+1, listx[i]))


def userSum(listx, num):
    sum = 0
    for i in range(num):
        sum += listx[i]
        print(listx[i], end =' ')

    print("total sum : ", sum)

