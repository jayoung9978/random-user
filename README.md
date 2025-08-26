# 테스트용 유저정보 랜덤 데이터 생성기

한국/외국 유저정보(이름, 주소, 이메일, 나이)를 랜덤으로 생성하는 웹/Python 프로그램입니다.

## 기능

- **다국어 지원**: 한국어/English 유저정보 생성
- **한국 데이터**: 실제 한국 성씨, 이름, 전국 주요 도시/구 주소
- **외국 데이터**: 영어권 이름, 미국 주소 형식
- **이메일 생성**: 이름 기반 이메일 주소 생성
- **웹 인터페이스**: HTML/JavaScript 기반 웹 버전 제공
- **다양한 출력**: 텍스트/JSON 형식 지원

## 사용법

### 1. 웹 버전 (권장)
1. `index.html` 파일을 브라우저에서 열기
2. 언어 설정 선택 (한국어/English)
3. 생성할 데이터 개수 입력
4. "데이터 생성하기" 버튼 클릭
5. 텍스트/JSON 형식 선택 후 복사

### 2. Python 버전
```bash
python3 random_generator.py
```

**메뉴 선택:**
- `1`: 이름만 생성
- `2`: 주소만 생성
- `3`: 이메일만 생성
- `4`: 전체 데이터 생성
- `5`: 여러 개 데이터 일괄 생성
- `0`: 프로그램 종료

### 3. Python 클래스 직접 사용
```python
from random_generator import RandomGenerator

generator = RandomGenerator()

# 개별 생성 (한국어만 지원)
name = generator.generate_korean_name()
address = generator.generate_korean_address()
email = generator.generate_email(name)

# 전체 데이터 생성
all_data = generator.generate_all_data()
print(all_data)
```

## 예시 출력

### 한국어 설정
```
[1번째 데이터]
이름: 김민준
이메일: kim3847@naver.com  
주소: 서울특별시 강남구 테헤란로 423
나이: 28
```

### English 설정
```json
[
  {
    "name": "James Smith",
    "email": "jamessmith2847@gmail.com",
    "address": "1234 Main St, New York, California 90210",
    "age": 32
  }
]
```

## 파일 구조

```
랜덤생성기/
├── index.html            # 웹 인터페이스 (권장)
├── random_generator.py   # Python 프로그램 
├── test_generator.py     # Python 테스트 파일
└── README.md            # 사용 설명서
```

## 데이터 소스

### 한국 데이터
- **성씨**: 한국 상위 40개 성씨
- **이름**: 최근 인기 있는 한국 이름들
- **주소**: 전국 16개 시도 + 주요 구/군 + 실제 도로명
- **이메일**: 주요 한국 이메일 도메인 (naver, daum, gmail 등)

### 외국 데이터
- **이름**: 영어권 인기 이름 (First Name + Last Name)
- **주소**: 미국 주요 도시/주 + 실제 거리명 + 우편번호
- **이메일**: 영어권 주요 도메인 (gmail, yahoo, outlook 등)

## 주요 특징

- ✅ **테스트 전용**: 실제 개인정보와 무관한 가상 데이터
- ✅ **다국어 지원**: 한국/미국 유저정보 형식
- ✅ **웹 기반**: 브라우저에서 바로 사용 가능
- ✅ **복사 기능**: 원클릭으로 클립보드에 복사
- ✅ **다양한 형식**: 텍스트/JSON 출력 지원

## 주의사항

- 생성된 데이터는 모두 가상의 데이터입니다
- 실제 개인정보와는 무관합니다
- **테스트 및 개발 목적으로만 사용하세요**