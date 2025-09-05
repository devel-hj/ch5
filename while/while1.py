# 반복문을 사용해서 똑같이 10번 출력하기

# 반복횟수를 결정하는 변수
# i = 0

# # 반복횟수를 결정하는 조건식
# while i < 5:
#     print('안녕하세요') # 반복하고 싶은 코드
#     i = i + 1 # i의 값을 변화시키는 코드


# 반복문 없이 1부터 10까지 출력
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# 반복문을 사용해 1부터 10까지 출력하세요
# i가 1부터 10까지 1씩 증가하면서
# 총 10번 반복 수행
# i = 1
# while i <= 10 :
#     # 출력할 수는 1부터 10까지 변화하는 수
#     print(i)
#     i += 1


# 반복문으로 숫자 3부터 6까지 출력하세요
# i = 3
# while i <= 6 :
#     print(i)
#     i += 1

# 반복문으로 "hello"을 5번 출력하세요
# i = 0
# while i < 5 :
#     print("hello")
#     i += 1

# # 반복문으로 숫자 1부터 7까지 출력
# i = 1
# while i <= 7 : 
#     print(i)
#     i += 1

# # 반복문으로 1 3 5 7 9 홀수 5개를 출력
# i = 0
# while i < 10 : 
#     if i % 2 == 1 :
#         print(i)
#         i += 1
#         continue
#     i += 1
    

# 반복문을 사용해서 11부터 20까지 출력
# i = 11
# while i <= 20 : 
#     print(i)
#     i += 1
# # 반복문을 사용해서 1부터 5까지 합을 출력
# i = 1
# sum = 0
# while i <= 5 : 
#     sum = sum + i
#     print('sum은',sum)
#     i += 1
# # 반복문으로 리스트의 요소를 하나씩 출력

# nums = [10, 20, 30]

# i = 0
# while i < len(nums) :
#     print(nums[i])
#     i += 1


# 1부터 20까지 더한 합구하기
# 합이 100을 넘으면 반복문을 종료
# i = 1
# sum = 0
# while i <= 20 :
#     if sum >= 100 :
#         break
#     sum = sum + i
#     i += 1
# print('합계: ',sum)

# lis = [100,77,-5,10]

# # 반복문으로 요소를 하나씩 출력하다가
# # 77을 만나면 break를 사용해 반복문을 종료하세요
# i = 0
# while i < len(lis) :
#     if lis[i] == 77 :
#         break 
#     print(lis[i])
#     i += 1


# 1부터 10까지 하나씩 출력하다가
# 3의 배수를 만나면 break를 사용해 반복문을 종료

# i = 0
# while i <= 10 :
#     i += 1
#     if i % 3 == 0:
#         break
#     print(i)

# lis = ['aa', 'bbb', 'ccccc', 'dd']

# # 반복문으로 요소를 하나씩 출력하다가 
# # 문자열의 길이가 4를 넘으면 반복문을 종료

# i = 0

# while i < len(lis) :
#     if len(lis[i]) > 4 :
#         break
#     print(lis[i])
#     i += 1

# # 반복문으로 1부터 10까지 출력
# # 짝수는 건너뛰고 홀수만 출력

# i = 1
# while i <=10 :
#     if i % 2 == 0:
#         print(i)
#         i += 1
#         continue
#     i+=1

# 리스트 생성
lis = [10, 'a', True, 20, 'b']

# while문으로 리스트의 요소를 하나씩 출력하세요
# 단, 숫자를 만나면 continue를 사용해 건너뛰세요
#

i = 0
while i < len(lis) :
    if type(lis[i]) == int:
        i += 1
        continue
    print(lis[i])
    i += 1


