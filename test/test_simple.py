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
    0 : "",
    4 : "만 ",
    8 : "억 ",
    12 : "조 ",
    16 : "경 ",
    20 : "해 ",
    24 : "자 "
}

a = ['3', '0', '0', '0', '0', '0', '0']
b = []

fcounter = 0
gcounter = len(a) - 1

for i in reversed(a):
    b.append(일의자리_한자어.get(int(i)))

    if (fcounter % 4 == 0) and (a[(gcounter - 3):(gcounter + 1)] != ['', '', '', '']):
        b[fcounter] = b[fcounter] + 더큰_자릿수.get(fcounter)
        b[fcounter].replace('일', '') # 추후에 if문 추가요망
    elif ((fcounter % 4) != 0) and (b[fcounter] != ''):
        b[fcounter] = b[fcounter] + 큰_자릿수.get(fcounter % 4)
    
    fcounter = fcounter + 1
    gcounter = gcounter - 1

list.reverse(b)

print((''.join(b)).rstrip())
