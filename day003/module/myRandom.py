#custom library

import random as rd

def radom_data(data):
    num = rd.choice(data)
    data.remove(num)
    return num

if __name__ == '__main__':
    data = [1,2,3,4,5]
    while data: print(radom_data(data))


data = [1,2,3,4,5]

print(data)
rd.shuffle(data)
print(data)

print(rd.randrange(1, 100))

#lotto program
num = []
winMsg = "you won!"

for i in range(0,6):
    num.append(rd.randrange(1, 2))

nums = input ("what your lotto number do you expect ? (delimiter is ,)").split(",")


print("lotto result is {}".format(num))
for i in range(0,6):
    if num[i] != int(nums[i]): winMsg = "sorry, next may be won...."

print(winMsg)