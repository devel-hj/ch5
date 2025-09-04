# 1부터 10까지 합 구하기
# 1+2+3+4+5+6+7+8+9+10 => 55
# sum = 1+2+3+4+5+6+7+8+9+10
# 대입연산
# 변수 = 값(식)
# sum = 0
# sum = sum + 1 # 0 + 1
# sum = sum + 2 # 1 + 2
# sum = sum + 3 # 3 + 3
# sum = sum + 4 # 6 + 4
# sum = sum + 5 # 10 + 5
# sum = sum + 6 # 15 + 6
# sum = sum + 7 # 21 + 7
# sum = sum + 8 # 28 + 8
# sum = sum + 9 # 36 + 9
# sum = sum + 10 # 45 + 10

# 반복하고 싶은 코드
# : sum = sum + ?
# 반복횟수 : 10번

# 반복문을 사용해 합 구하기
i = 1
sum = 0

while i < 11 :
    sum = sum + i
    i += 1

print('합: ', sum)