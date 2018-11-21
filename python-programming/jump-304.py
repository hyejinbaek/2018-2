#점프투파이썬 304쪽 match
import re
p=re.compile('[a-z]+')
print(p)

m=p.match("python")
print(m)

print(re.compile("[a-z]+").match("python").group())