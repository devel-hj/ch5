# 반복문으로 1부터 20까지 합 구하기
# 단, 함이 100을 넘으면 while문을 중단

# while문 안에서 break를 만나면
# 반복횟수가 끝나지 않았어도 while문 중단
# sum = 0
# i = 1

# while i <= 20 :
#     sum = sum + i
#     if sum > 100 :
#         print('마지막 sum:', sum) # 105
#         print('마지막 i:', i) # 14
#         break
#     i += 1

# 디버깅
sum = 0
i = 1

while i <= 20 :
    sum = sum + i
    if sum > 100 :
        break
    i += 1