# import 뭐시기

수사_종류 = ["양수사", "양수사-관형사", "서수사", "서수사-명사"]

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

일의자리_고유어 = {
    0 : '',
    1 : '하나',
    2 : '둘',
    3 : '셋',
    4 : '넷',
    5 : '다섯',
    6 : '여섯',
    7 : '일곱',
    8 : '여덟',
    9 : '아홉'
}

일의자리_고유어_관형사 = {
    0 : '',
    1 : '한',
    2 : '두',
    3 : '세',
    4 : '네',
    5 : '다섯',
    6 : '여섯',
    7 : '일곱',
    8 : '여덟',
    9 : '아홉'
}

십의자리_고유어 = {
    0 : "",
    1 : "열",
    2 : "스물",
    3 : "서른",
    4 : "마흔",
    5 : "쉰",
    6 : "예순",
    7 : "일흔",
    8 : "여든",
    9 : "아흔"
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

def convert(number, 수사="양수사", 한자어=True):
    if 수사 not in 수사_종류:
        raise NotImplementedError('없는 수사 종류에요 ㅜㅜ')

    if isinstance(number, (str, float)): #소수점 이하 읽기 추후 구현 예정
        number = int(number)
    if isinstance(number, (list, dict, tuple)):
        raise TypeError('잘못된 자료형이에요 ㅜㅜ')
    if number >= 10000000000000000000000000000:
        raise ValueError('너무 큰 수에요 ㅜㅜ')
    if isinstance(한자어, bool) == False:
        raise TypeError('잘못된 자료형이에요 ㅜㅜ')

    # return [number, 수사, 한자어] - 테스트용

    if 한자어 == True:
        return _한자어(number)
    else:
        pass
        # return _고유어(number)

##########################################
## 스위치(?)
##########################################

def _한자어(hnum):
    return _구현(str(hnum))

def _고유어(gnum):
    pass

def _관형사(anum):
    pass
    
def _명사(mnum):
    pass

##########################################
## 구현
##########################################

def _구현(gnum):
    a = []
    b = []
    for i in gnum:
        for x in i:
            a.append(x)

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

    return (''.join(b)).rstrip()
