

class Score:

    sum = 0
    avg = 0

    math = 0
    kor = 0
    eng = 0

    def __init__(self):
        r = input('국어, 영어 수학 점수를 입력하세요: (구분은 ,으로)')
        elements = r.split(',')
        self.kor = elements[0]
        self.eng = elements[1]
        self.math = elements[2]

    def total(self):
        self.sum = int(self.kor) + int(self.eng) + int(self.math)

    def avg(self):
        self.avg = self.sum /3




s = Score()



sum = s.total()
avg = s.avg()
print('총점 {}  평균 {}'.format( s.sum, s.avg) )
