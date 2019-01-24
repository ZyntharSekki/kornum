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

더큰_자릿수 = {
    4 : "만 ",
    8 : "억 ",
    12 : "조 ",
    16 : "경 ",
    20 : "해 ",
    24 : "자 "
}

a = str(input("입력바람: "))
list_00 = []
list_01 = []
list_02 = []

for i in a:
    for x in i:
        list_00.append(x)

for i in list_00:
    list_01.append(일의자리_한자어.get(int(i)))

print(list_01)

for i in range(0, len(list_01)):
    if len(list_01) >= 4:
        rtemp = list_01[-4:]
        rtemp1 = list_01[-4:]
        for i2 in range(0, 4):
            itemp = rtemp.pop()
            list_01.pop()
            if(itemp == ''):
                list_02.append(itemp)   
            elif(itemp == '일'):
                if i2 == 0:
                    list_02.append(itemp)
                else:
                    list_02.append(큰_자릿수.get(i2))
            else:
                list_02.append(itemp + 큰_자릿수.get(i2))
    else:
        pass
        
for i in range(0, len(list_02)):
    print(i)
    if ((i in 더큰_자릿수) == True):
        if list_02[i:i+4] == ['', '', '', '']:
            pass
        else:
            list_02[i] = list_02[i] + 더큰_자릿수.get(i)

print(list_02)

맅턴 = str()

for i in range(0, len(list_02)):
    맅턴 = 맅턴 + list_02.pop()

print(맅턴)
