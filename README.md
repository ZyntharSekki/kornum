kornum
====

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

kornum은 숫자를 한국어 단어로 바꿔주는 모듈입니다.

**개발중-고유어 서수사 구현 안 됨**

# 사용법
## 양수사
```
>>> kornum.convert(69, 수사='양수사', 한자어=True)
'육십구'
```
한자어

```
>>> kornum.convert(74, 수사='양수사', 한자어=False)
'일흔넷'
```
고유어

### 관형사
```
>>> kornum.convert(74, 수사='양수사-관형사', 한자어=False)
'일흔네'
```

## 서수사
```
>>> kornum.convert(42, 수사='서수사', 한자어=True)
'제사십이'
```
한자어

```
>>> kornum.convert(42, 수사='서수사', 한자어=False)
'마흔두째'
```
고유어

### 명사
```
>>> kornum.convert(42, 수사='서수사-명사', 한자어=False)
'마흔둘째'
```
# 라이선스

MIT 라이선스

# 기타
코딩 초짜라 구조가 많이 허접할 수 있습니다

## 제작 이유
연습용 + [num2words](https://github.com/savoirfairelinux/num2words)의 한국어 모듈이 마음에 안 들었음
