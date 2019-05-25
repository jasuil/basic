#file

f = open("myFile.txt",'w')

for i in range(1, 11):
    data = '{} th line\n'.format(i)
    f.write(data)

f.close()

f = open("myFile.txt",'r')

while True:

     txt = f.readline(-1)
     if(len(txt) == 0):
         break
     else:
        print(txt)


f.close()