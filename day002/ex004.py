# import
import datetime

now = datetime.datetime.now()
today = now.timetuple() #년/월/일
year = today[0] #년도만 추출

print('this year is ', year)

print(year % 4 == 0 and ((year % 100 != 0) or (year % 400 == 0)))

print('##################################')

if year % 4 == 0 and ((year % 100 != 0) or (year % 400 == 0)):
    print('{}은 윤년'.format(year))
else:
    print('{}은 평년'.format(year))