#수강생 장성일
#1~100 까지 3의 배수 출력 및 누적합(for if)

sum = 0
ind = 1;
for i in range(1, 101):
    if(i % 3 ) == 0:
        print("3의 {}번째 배수입니다.  {}".format(ind, i))
        sum += i
        ind += 1

print("accumulate sum is {}".format(sum))



#년도 입력 받아서 윤년/평년 판정 프로그램 작성 (if else)

resultMsg = "평년입니다."
inputYear = int(input("input year "))

if(inputYear % 4 ) == 0:
    if((inputYear % 100) != 0) | ((inputYear % 400) == 0):
        resultMsg = "윤년입니다."
    else:
        pass
else:
    pass

print("{}는 {}".format(inputYear, resultMsg))