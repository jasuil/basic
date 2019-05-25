#nested if clause


var = 100
if var < 200:
    print("expression value is less than 200")
    if var == 150:
        print("which is 150")
    elif var == 100:
        print("which is 100")
    elif var == 50:
        print("which is 50")
elif var < 50:
    print("expression value is less than 50")
else:
    print("Could not find true expression")

print("the end")


# judge even or odd and positive or negative

yourNum = int(input("input your number?"))
neg = "양수"
even = "짝수"

if yourNum > 0:
    pass
elif yourNum < 0:
    neg = "음수"
else:
     neg = "양수도 음수도 아님 "

if(yourNum % 2) == 1:
    even = "홀수"
else:
    pass

print("{} is  {} and {}".format(yourNum, even, neg))