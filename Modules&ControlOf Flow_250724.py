from math import ceil, floor, pi

PI = pi
print(ceil(PI)) # 올림
print(floor(PI)) # 내림
print(round(PI)) # 반올림



# json과 dict의 공통점
# key: value 쌍
# 차이점
# json은 반드시 key값이 문자열, 큰따옴표


# .json --> 딕셔너리?
# response 



# 파이써닉하다
arr = [0] * 5

# i = 0, 1, 2, 3, 4
# i + 5
for i in range(5):
    arr[i] = i + 5

for num in arr: # iterator 방식 순회
    print(num, end = ' ')
