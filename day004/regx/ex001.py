# regx

import re

source = "ct cat caat caaat caaaat caaaaat caaaaaat"

m1 = re.findall("ca{2}t", source)
m2 = re.findall("ca{2,5}t", source)
m3 = re.findall("ca{0,}t", source)
m4 = re.findall("ca{0,1}t", source)
m5 = re.findall("ca{,1}t", source)
m6 = re.findall("ca?", source)

print("m1: {}".format(m1))
print("m2: {}".format(m2))
print("m3: {}".format(m3))
print("m4: {}".format(m4))
print("m5: {}".format(m5))
print("m6: {}".format(m6))
