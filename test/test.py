일의자리_한자어 = {
    0 : '',
    1 : '일',
    2 : '이',
    3 : '삼',
    4 : '사',
    5 : '오',
    6 : '육',
    7 : '칠',
    8 : '팔',
    9 : '구'
}

큰_자릿수 = {
    0 : "",
    1 : "십",
    2 : "백",
    3 : "천"
}

a = str(input("입력바람: "))
result = []
b = []

for i in a:
    for x in i:
        b.append(x)

for i in b:
    result.append(일의자리_한자어.get(int(i)))

theresult = []

for i in range(0, len(result)):
    if len(result) >= 4:
        rtemp = result[-4:]
        for i in range(0, 4):
            itemp = rtemp.pop()
            if(itemp == ''):
                theresult.append(itemp)   
            elif(itemp == '일'):
                if i == 0:
                    theresult.append(itemp)
                else:
                    theresult.append(큰_자릿수.get(i))
            else:
                theresult.append(itemp + 큰_자릿수.get(i))
        for i in range(0, 4):
            result.pop()


print(theresult)
