# 가변인자 여러개

def varF(init = 0, *num, **dict):

    count = init

    for n in num:
        count += n


    for key in dict:
        count += dict[key]

    return count

rCount = varF(10,1,2,3, vegetable = 100, fruits = 200)

print('total count is {}'.format(rCount))
