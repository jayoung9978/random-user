# 랜덤 데이터 생성기

한국식 이름, 전화번호, 주소, 숫자를 랜덤으로 생성하는 Python 프로그램입니다.

## 기능

- **한국 이름 생성**: 실제 한국 성씨와 이름을 조합하여 자연스러운 이름 생성
- **전화번호 생성**: 010-XXXX-XXXX 형식의 휴대폰 번호 생성
- **주소 생성**: 서울특별시 기준 실제 구/도로명을 사용한 주소 생성
- **랜덤 숫자**: 지정된 범위 내의 랜덤 숫자 생성
- **이메일 생성**: 생성된 이름 기반의 이메일 주소 생성
- **일괄 생성**: 모든 데이터를 한 번에 생성

## 사용법

### 1. 프로그램 실행
```bash
python random_generator.py
```

### 2. 메뉴 선택
- `1`: 이름만 생성
- `2`: 전화번호만 생성  
- `3`: 주소만 생성
- `4`: 랜덤 숫자 생성 (범위 지정 가능)
- `5`: 이메일만 생성
- `6`: 전체 데이터 생성 (이름, 전화번호, 이메일, 주소, 나이, 점수 등)
- `7`: 여러 개 데이터 일괄 생성
- `0`: 프로그램 종료

### 3. 클래스 직접 사용
```python
from random_generator import RandomGenerator

generator = RandomGenerator()

# 개별 생성
name = generator.generate_korean_name()
phone = generator.generate_phone_number()
address = generator.generate_korean_address()
number = generator.generate_random_number(1, 100)

# 전체 데이터 생성
all_data = generator.generate_all_data()
print(all_data)
```

## 예시 출력

```
=== 생성된 데이터 ===
이름: 김민준
휴대폰: 010-3847-2951
이메일: kim2847@gmail.com  
주소: 서울특별시 강남구 테헤란로 423, 1205호
랜덤숫자: 742
나이: 28
점수: 85
```

## 파일 구조

```
랜덤생성기/
├── random_generator.py    # 메인 프로그램
└── README.md             # 사용 설명서
```

## 데이터 소스

- **성씨**: 한국 상위 40개 성씨
- **이름**: 최근 인기 있는 한국 이름들
- **주소**: 서울특별시 25개 구 + 실제 도로명
- **이메일**: 주요 한국 이메일 도메인

## 주의사항

- 생성된 데이터는 모두 가상의 데이터입니다
- 실제 개인정보와는 무관합니다
- 테스트 용도로만 사용하세요