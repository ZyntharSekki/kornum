"testing"

수사_종류 = ["양수사", "양수사-관형사", "서수사", "서수사-명사"]


def convert(number, 수사="양수사", 한자어=True):
    if isinstance(number, (str, float)): #소수점 이하 읽기 추후 구현 예정
        number = int(number)
    if isinstance(number, (list, dict, tuple)):
        raise TypeError('잘못된 자료형이에요 ㅜㅜ')
    if 수사 not in 수사_종류:
        raise NotImplementedError('없는 수사 종류에요 ㅜㅜ')

    return [number, 수사, 한자어]
