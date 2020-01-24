#file, absolute path

#f = open("d:\\파이썬 기초반\\sample.txt", "w")
f = open("d:/파이썬 기초반/sample.txt", "w")
f.write("성일짱\n")
f.write("짱성일\n")
f.write("1212\p \'안뇽\' \"")
f.close()

f = open("d:/파이썬 기초반/sample.txt", "r")
str = f.read()
f.close()


