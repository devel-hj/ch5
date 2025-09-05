# while문 안에서 continue를 만나면
# 더이상 아래 코드를 생행하지 않고
# 다시 반복문으로 돌아간다

# 1부터 10까지 출력하기
# 단, 짝만 출력할것
# => 홀수는 생략

i = 1
while i <= 10 :
    if i % 2 == 1 :
        i += 1
        continue
    print(i)
    i += 1