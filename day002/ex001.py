# while
fruits = ['apple', 'banana', 'orange']
i=0 #while문을 위한 변수 초기화

while i < len(fruits):
    print(fruits[i])
    i += 1


###########################

# 문제2 : 별모양의 산 출력

i=0
s='*'
while i<5:
    print(s)
    s += '*'
    i += 1


###########################

# average

lists = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
i = 0
sum = 0
average = 0
score = 0

for score in lists:
    sum += score


average = sum / len(lists)
print('average is {}'.format(average))