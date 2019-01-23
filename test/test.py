일의자리_한자어 = {
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
    10 : "십",
    100 : "백",
    1000 : "천"
}

a = str(input("입력바람: "))
result = []
b = []

for i in a:
    for x in i:
        b.append(x)

for i in range(0, len(b)):
    result.append(일의자리_한자어.get(int(b.pop())))

print(result)
