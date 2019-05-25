f = open("jumsu.txt", 'r')
sum = 0
count = 0
avg = 0

while True:
    lines = f.readline()

    f2 = open("avg_result.txt", 'w')

    if not lines: break
    sum += int(lines)
    count += 1

avg = sum/count
print('average is {:.2f}'.format(avg))

f2.write("average is {}".format('average is {:.2f}'.format(avg)))
f2.close()
