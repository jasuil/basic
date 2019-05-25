#file

# while 1:
#     dat = input()
#
#     if not dat: break
#
#     print(dat)


f = open('myFile.txt', 'r')

while True:
    data = f.readlines()
    if not data: break
    print(data)

f.close()