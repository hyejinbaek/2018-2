#점프투파이썬 334쪽 Q4

import re
data = """
kim,fail,fail
shin,pass,fail
"""

pat = re.compile("(\w+[,]\w+[,])\w+")

print(pat.sub("\g<1>pass", data))