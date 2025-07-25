print('hello, world', end='') 
print('world')

degree = 36.5
print(id(degree))

degree = 36.6
print(id(degree))


# 변수명 규칙 : 숫자로 시작할 수 없다.
# 언더스코어 가능 : 언더스코어로 시작할 수 있다.
# 키워드 사용 불가능 (if, for)
# 내장함수나 메서드를 가급적 사용하지 않는다.
# 대소문자는 서로 다른 유니코드값을 가지고 있다. (서로 아예 다른 값이다)


a = 1
b = 2.0
c = 3 + 2j
d = '1'

# 정수(int) = 음의 정수, 양의  정수, 0

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# 1억을 지수 표현법으로

# num = 1e8
# print(num)

num = (-2) ** 3
print(num)


print('\'안녕\n하세요\'')

name = '이승연'
age = 20
height = 185.76312

print(f'제 이름은 {name}이고 나이는 {age}살, 키는 {height:.2f} 입니다.')


