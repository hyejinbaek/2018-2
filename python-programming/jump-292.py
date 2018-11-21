#점프투파이썬 292쪽 문자열압축하기 문제
strInput = "aaabbcccccca"
stroutput = "a3b2c6a1"

curChar = ""
count = 0

for i in strInput:
    if curChar == i:
        count = count + 1
    else :
        if count != 0:
            print(curChar, i)
            count = 1

    curChar = i

print(curChar, i)

print(curChar, count)