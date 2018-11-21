#점프투파이썬 292쪽 문자열압축하기 문제
enter = input("문자열 입력하세요 ")
a = ''
c=0
for i in enter:
    if(a==i):
        c += 1
    else :
        if c != 0:
            print(a + str(c) , end='')
        a=i
        c=0
        c += 1

print(a + str(c))