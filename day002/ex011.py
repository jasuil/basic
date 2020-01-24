# calc

def add(*num):
    i = 0

    for n in num:
        i += n

    print('add result is ', i)


def sub(a, b):

    print('subtraction is ', (a - b))


def mul(*num):
    i = 1

    for n in num:
        i *= n


    return i


def div(a, b):

     return a/b


add(3,-23)
sub(1, -0.3)
num = (1,2,3, 4,54)
print('{} multiplication is {}'.format(num, mul(1,2,3, 4,54)))

print('{} / {} division is {}'.format(2, 4, div(2, 4)))