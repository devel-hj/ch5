# # 퀴즈

# # 다음과 같이 리스트를 만들고
# # for문으로 요소를 하나씩 출력하세요
# mixed = [1, 'apple', 3.14, True]

# # for 변수 in 자료구조(list tuple div iter)
# for m in mixed :
#     print(m)

# # 다음과 같이 리스트를 만들고 
# # for문으로 요소를 하나씩 출력하세요
# fruits = ['apple', 'banana', 'cherry']

# for f in fruits:
#     print(f)

# # 다음과 같이 딕셔너리를 만들고 
# # for문으로 key를 하나씩 출력하세요
# students = {"이름": "둘리", "나이": 20, "주소": "인천"}

# for key in students :
#     print(key)

# # 다음과 같이 딕셔너리를 만들고 
# # for문으로 value를 하나씩 출력하세요
# coffee_menu = {"아메리카노": "2500원", "라떼": "3000원", "케이크": "4500원"}

# for value in coffee_menu.values():
#     print(value)


# for문을 사용해서 11부터 20까지 출력하세요
# for n in range(11, 20 + 1) :
#     print(n)

# # for문을 사용해서 5부터 15까지 출력하세요
# for n in range(5, 15 + 1) :
#     print(n)

# # for문을 사용해서 'hi' 5번 출력하세요
# for _ in range(5) :
#     print('hi')

# num = [10, 20, 30, 40, 50]
# for문으로 모든 요소를 더해서 합을 구하세요

# sum = 0
# for n in num :
#     sum = sum + n
#     print(sum)


# for문을 사용해서
# 1부터 100까지 숫자 중에서 3의 배수만 출력하세요
# for n in range(1, 100 + 1) : 
#     if n % 3 == 0 :
#         print(n)


# 변수n을 선언하고 숫자를 대입하세요
# n의 크기만큼 *별을 출력하세요
# 예) n=5 => *****
# 예) n=3 => ***

# num = 5

# # 문자열 반복 연산 사용
# print( '*' * num) # *****

# # for문 사용
# str1 = '' # 결과를 저장할 변수
# for _ in range(num) :
#     str1 = str1 + '*'

#     print(str1)


# 변수n을 선언하고 숫자를 대입하세요
# n의 크기만큼 삼각형을 그려주세요
# n=3
# =>

# *
# **
# ***

# num = 5

# for i in range(1, num + 1) :
    # print('*' * i)


#     *
#    **
#   ***
#  ****
# *****
# for i in range(1, 6):
#     print(' ' * (5-i) + '*' * (i)) # 공백과 별의 조합

# 구구단 중에서 3단을 출력
# num = 3
# for i in range(1, 10):
    # print( num,'x',i,'=', num * i )

