# 한 줄 문자열 정의
import math

s = ''
str1 = 'Hello World'
print(type(s), type(str1))
print(isinstance(str1, str))

# 여러 줄 문자열
str2 = '''ABC
1234
가나다라'''

print(str2)

''' 
    여기는 주석입니다.
    여러 라인 주석을 대체할 수 있습니다.
'''

# escape
print("Hello\nWorld\n! Say \"Hello World\"")

#
# 문자열 연산
#

# 1. 인덱싱
str1 = 'First String'
str2 = 'Second String'

print(str1[0], str1[1], str1[2])
print(str1[-1], str1[-2], str1[-3])

# 2. Slicing
# s[start:stop:step]
str3 = str2[2:5]
print(str3)
# print(str2[2:len(str2):1])
print(str2[2:])

s = "Python"
print(s[-1])        # 마지막 문자
print(s[-2:])       # 마지막 2개 문자
print(s[:-2])       # 마지막 2개 문자를 제외한 전체 문자열
print(s[::-1])      # Reverse
print(s[1::-1])     # 1 인덱스 부터 역순으로 가져온다. s[1:0:-1]
print(s[:-3:-1])    # 끝에서부터 역순으로 -3 인덱스까지.
print(s[-3::-1])

# 연결(+)
print(str1+str2)
print(str1, str2, sep=' ')
# 리터럴 연결시 + 생략 가능
# str3 = '1st' + ' ' + '2nd'
str3 = '1st' ' ' '2nd'
print(str3)

# 문자열 객체 연결은 문자열끼리만 할 수 있다.
name = '둘리'
age = 10
# print(name + 10)

# 반복(*)
print(str1 * 3)

# len() 함수
print(len(str1))

# in, not in 연산
print('F' in str1)
print('S' not in str1)

# str 객체는 Immutable 이다.
# str1[0] = 'f'

# 서식(formatting) = format 함수
print('name : ' + name + ', age : ' + str(age))
print('name : ' + format(name, "s") + ', age : ' + format(age, "d"))

# 서식 : 튜플 사용
f = "name : %s, age : %d"
print(f % (name, age))
print(f % ("또치", 20))

# 서식 : 딕셔너리 사용
f = "name : %(n)s, age : %(a)d"
print(f % {'n': '둘리', 'a': 20})

#
# 객체함수
#

# 1. 대소문자 관련
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())   # 맨 앞만 대문자로.
print(s.title())        #

# 2. 검색
s = 'I Like Python, I Like Java Also'
print(s.count('Like'))    # 문자열 찾기
print(s.find('Like'))     # 문자열이 시작되는 인덱스
print(s.find('Like', 5))  # 시작위치 지정
print(s.find('JavaScript'))
print(s.rfind('Like'))    # Reverse Find

# print(s.index('JavaScript'))  # index 함수는 지정 문자가 없을 경우 익셉션을 발생시킨다.
# print(s.rindex('JavaScript'))

print(s.startswith("I Like"))   # 지정 문자로 시작하냐
print(s.startswith("Like", 2))
print(s.endswith("Also"))
print(s.endswith("Java", 0, 20))  # 지정 인덱스 사이가 해당 문자로 끝나냐


# 편집과 치환
s = '     spam and ham     '
print('-----' + s.strip() + '------')   # 공백 제거
print('-----' + s.rstrip() + '------')   # r / l 공백 제거

s = '<><abc><><defg><><>'
print('-----' + s.strip('><') + '------')   # 특정 패턴을 제거할 수 있다.
print('-----' + s.strip('<>') + '------')

s = 'Hello Java'
print(s.replace('Java', 'Python'))

# 분리 & 결합
s = 'spam and ham'
l = s.split(' and ')   # 지정 문자 기준으로 나눈다.
print(l, type(l))

s2 = ':'.join(l)  # 지정 문자로 리스트를 결합한다.
print(s2)

s3 = 'one:two:three:four:five'
print(s3.split(':'))
print(s3.split(':', 2))   # 지정 수만큼까지 쪼개고 나머지는 하나의 문자로서 리스트에 넣는다.
print(s3.rsplit(':', 2))  # r / l                     ||

lines = '''1st line
2nd line
3rd line
4th line
'''

print(lines.split('\n'))
print(lines.splitlines())


# 판별
print('abcd'.islower())
print('abcd'.isupper())

print('    '.isspace())
print('\r\n'.isspace())
print('\t'.isspace())

# '0' 채우기
print('20'.zfill(5))
print('1234'.zfill(5))

# 서식 : 객체 함수
print('name:{}, age{}'.format('둘리', 10))
print('name:{0}, age{1}'.format('둘리', 10))
print('name:{1}, age{0}'.format(10, '둘리'))
print('{:3}의 제곱근은 {:.7}'.format(2, math.sqrt(2)))
print('name:{n}, age{a}'.format_map({'a': 20, 'n': '둘리'}))

