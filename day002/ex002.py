# 구구단

#use for
for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        print(' {} x {} = {}'.format(i, j, (i*j)) )


print('***********************************************')
print('********************** use while *************************')

#use while
i = 1
while i < 10:
    j = 1
    while j < 10:
        print('{} x {} = {}'.format(i, j, (i*j)) )
        j += 1
    i += 1
