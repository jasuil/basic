#
import sys

with open('myExample.txt', 'w') as file:
    data = file.write("python basic grammar")

try:
    f = open("myExample2.txt", 'r')
    text = f.read()
    print(text)
    f.close()
except FileNotFoundError:
    print(sys.stderr)
    #f.write("file reading error ", sys.stderr)


