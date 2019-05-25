#file read

f2 = open('myFile.txt', 'r')

while True:
    readLine = f2.read()
    if not readLine: break
    print(readLine)

########################################
#file with

with open('myFile.txt', 'a') as f:
    f.write("짱성일~p")



#append data
with open('myFile.txt', 'a') as f:
    for element in range(11, 20):
        data = '{} th line\n'.format(element)
        f.write(data)


print('the end')