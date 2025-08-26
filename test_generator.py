#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
테스트용 유저정보 랜덤 데이터 생성기
"""

from random_generator import RandomGenerator

def test_generator():
    generator = RandomGenerator()
    
    print("=== 테스트용 유저정보 랜덤 데이터 생성기 ===\n")
    
    # 각 기능 테스트
    print("1. 이름 생성:")
    for i in range(3):
        print(f"   {generator.generate_korean_name()}")
    
    print("\n2. 전화번호 생성:")
    for i in range(3):
        print(f"   {generator.generate_phone_number()}")
    
    print("\n3. 주소 생성:")
    for i in range(3):
        print(f"   {generator.generate_korean_address()}")
    
    print("\n4. 이메일 생성:")
    for i in range(3):
        print(f"   {generator.generate_email()}")
    
    print("\n5. 랜덤 숫자 생성 (1-100):")
    for i in range(3):
        print(f"   {generator.generate_random_number(1, 100)}")
    
    print("\n6. 전체 데이터 생성:")
    for i in range(2):
        data = generator.generate_all_data()
        print(f"\n[{i+1}번째 데이터]")
        for key, value in data.items():
            print(f"   {key}: {value}")

if __name__ == "__main__":
    test_generator()