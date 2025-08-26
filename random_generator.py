#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
테스트용 유저정보 랜덤 데이터 생성기
이름, 숫자, 주소를 랜덤으로 생성합니다.
"""

import random
import string

class RandomGenerator:
    def __init__(self):
        # 한국 성씨
        self.last_names = [
            '김', '이', '박', '최', '정', '강', '조', '윤', '장', '임',
            '한', '오', '서', '신', '권', '황', '안', '송', '류', '전',
            '홍', '고', '문', '양', '손', '배', '조', '백', '허', '유',
            '남', '심', '노', '정', '하', '곽', '성', '차', '주', '우'
        ]
        
        # 한국 이름
        self.first_names = [
            '민준', '서준', '예준', '도윤', '시우', '주원', '하준', '지호', '건우', '우진',
            '지민', '서연', '서윤', '지우', '하윤', '예은', '지유', '윤서', '채원', '시은',
            '소율', '지아', '예린', '수빈', '다은', '채윤', '하은', '수아', '예나', '유나',
            '현우', '준서', '민재', '준혁', '지훈', '태윤', '민성', '연우', '정우', '승우'
        ]
        
        # 서울 구 목록
        self.districts = [
            '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구',
            '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구',
            '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
        ]
        
        # 도로명
        self.road_names = [
            '가로수길', '강남대로', '테헤란로', '올림픽로', '한강대로', '서초대로',
            '논현로', '압구정로', '삼성로', '역삼로', '언주로', '봉은사로',
            '세종대로', '종로', '을지로', '퇴계로', '동작대로', '여의대로',
            '양화로', '홍익로', '연남로', '성산로', '증산로', '공항대로'
        ]

    def generate_korean_name(self):
        """한국 이름 생성"""
        last_name = random.choice(self.last_names)
        first_name = random.choice(self.first_names)
        return f"{last_name}{first_name}"


    def generate_korean_address(self):
        """한국 주소 생성"""
        district = random.choice(self.districts)
        road = random.choice(self.road_names)
        building_num = random.randint(1, 999)
        
        return f"서울특별시 {district} {road} {building_num}"

    def generate_email(self, name=None):
        """이메일 주소 생성"""
        if name is None:
            name = self.generate_korean_name()
        
        domains = ['gmail.com', 'naver.com', 'daum.net', 'hanmail.net', 'yahoo.co.kr']
        
        # 한글 이름을 영문으로 변환 (간단한 방식)
        name_mapping = {
            '김': 'kim', '이': 'lee', '박': 'park', '최': 'choi', '정': 'jung',
            '강': 'kang', '조': 'jo', '윤': 'yoon', '장': 'jang', '임': 'lim'
        }
        
        last_char = name[0]
        eng_last = name_mapping.get(last_char, 'user')
        random_num = random.randint(100, 9999)
        domain = random.choice(domains)
        
        return f"{eng_last}{random_num}@{domain}"

    def generate_all_data(self):
        """모든 데이터를 한 번에 생성"""
        name = self.generate_korean_name()
        return {
            '이름': name,
            '이메일': self.generate_email(name),
            '주소': self.generate_korean_address(),
            '나이': random.randint(18, 65)
        }

def main():
    generator = RandomGenerator()
    
    print("=== 랜덤 데이터 생성기 ===\n")
    
    while True:
        print("1. 이름 생성")
        print("2. 주소 생성")
        print("3. 이메일 생성")
        print("4. 전체 데이터 생성")
        print("5. 여러 개 데이터 생성")
        print("0. 종료")
        
        choice = input("\n선택하세요 (0-5): ")
        
        if choice == '1':
            print(f"생성된 이름: {generator.generate_korean_name()}")
            
        elif choice == '2':
            print(f"생성된 주소: {generator.generate_korean_address()}")
            
        elif choice == '3':
            print(f"생성된 이메일: {generator.generate_email()}")
            
        elif choice == '4':
            data = generator.generate_all_data()
            print("\n=== 생성된 데이터 ===")
            for key, value in data.items():
                print(f"{key}: {value}")
                
        elif choice == '5':
            count = int(input("생성할 데이터 개수: ") or "5")
            print(f"\n=== {count}개 데이터 생성 ===")
            for i in range(count):
                data = generator.generate_all_data()
                print(f"\n[{i+1}번째 데이터]")
                for key, value in data.items():
                    print(f"{key}: {value}")
                    
        elif choice == '0':
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("잘못된 선택입니다.")
        
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()