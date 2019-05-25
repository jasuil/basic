#test

# 성적 구하기
name = input("input your name?")
#scoreA = input("english score?")
#scoreB = input("math score?")
score = input("input your english, math score with space (ex 34 23)? ").split(" ")

#total = int(scoreA) + int(scoreB)
total = int(score[0]) + int(score[1])
average = total/2

grade = 'A'

if total >= 90:
    grade = 'A'
elif total >= 80:
    grade = 'B'
elif total >= 70:
    grade = 'C'
elif total >= 60:
    grade = 'D'
elif total >= 50:
    grade = 'E'
else:
    grade = 'F'


print("{} \nyour grade is {} \nyour total score is {}\naverage is {:.2f}".format(name, grade, total, average))