import random
#if clause

'''
var1 = 175
if var1:
    print('ok, you got it')
    print(var1)

var2 = 0
if var2:
    print("oh, shit !!!")
elif var2 < 0:
    pass
else:
    print("oh, my man")

'''
score = random.randrange(1,100)

if score >= 93:
    print("A")
elif score >= 84:
    print("B")
elif score >= 77:
    print("C")
elif score >= 60:
    print("D")
elif score >= 40:
    print("E")
else:
    print("F, fuck!")

print("the end, your score is ", score)