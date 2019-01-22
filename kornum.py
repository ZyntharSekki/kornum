"testing"

수사_종류 = ["양수사", "양수사-관형사", "서수사", "서수사-명사"]


def convert(number, 수사="양수사", 한자어=True):
    if isinstance(number, str):
        number = int(number)
    if 수사 not in 수사_종류:
        raise NotImplementedError('없는 수사 종류에요 ㅜㅜ')

    return [number, 수사, 한자어]
