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
    list_00 = []
    list_01 = []
    list_02 = []

    for i in gnum:
        for x in i:
            list_00.append(x)

    for i in list_00:
        list_01.append(일의자리_한자어.get(int(i)))

    if ((len(list_01) % 4) != 0):
        for ib in range(0, (4 - (len(list_01) % 4))):
            list_01.insert(0, '')

    for i in range(0, int(len(list_01) / 4)):
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
        
    for i in range(0, len(list_02)):
        if ((i in 더큰_자릿수) == True):
            if list_02[i:i+4] == ['', '', '', '']:
                pass
            elif list_02[i] == '일':
                list_02[i] = 더큰_자릿수.get(i)
            else:
                list_02[i] = list_02[i] + 더큰_자릿수.get(i)

    리턴값 = str()

    for i in range(0, len(list_02)):
        리턴값 = 리턴값 + list_02.pop()
    
    리턴값.rstrip()
    
    return 리턴값
