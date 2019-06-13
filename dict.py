# 생성
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

# 접근
print(d['basketball'])

# 변경 가능 (mutable)
d['valleyball'] = 6
print(d)

# 반복(*), 연결(+) 지원하지 않는다(sequence 형이 아니기 때문)

# 길이
print(len(d))

# in, not in 가능 : 키만 가능
print('soccer' in d)
print('valleyball' in d)

#
# 다양한 dict 객체 생성 방법
#

# 1. literal
d = {}
print(type(d))

# 2-1. dict() 사용하는 방법 1
d = dict()
print(d)

# 2-2. dict() 사용하는 방법 2
d = dict(one=1, two=2, three=3)
print(d)

# 2-3. dict() 사용하는 방법 3
d = dict([('one', 1), ('two', 2), ('three', 3)])
print(d)

# 2-4 dict() 사용하는 방법 4 - zip 사용
keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values))
print(d)

# 다양한 key 타입 (Immutable 타입만 사용 가능)
d = {}
d[True] = 'true'
d[10] = '10'
d['twenty'] = 20
d[(1, 2, 3)] = 6
# d[[1, 2, 3]] = 6
print(d)

# keys 객체
keys = d.keys()
print(keys, type(keys))
for key in keys:
    # print(key, type(key))
    print("{0} : {1}".format(key, d[key]))

# values 객체
values = d.values()
print(values, type(values))

# items 객체
# [(key1, value1), (key2, value2) .... ]
items = d.items()
print(items, type(items))

phone = {
    '둘리': '000-0000-0000',
    '마이콜': '111-1111-1111',
    '고길동': '222-2222-2222'
}
p = phone
print(p)
print(phone)
p['도우넛'] = '333-3333-3333'
print(p)
print(phone)

phone = {
    '둘리': '000-0000-0000',
    '마이콜': '111-1111-1111',
    '고길동': '222-2222-2222'
}
p = phone.copy()
print(p)
print(phone)
p['도우넛'] = '333-3333-3333'
print(p)
print(phone)

# get() 함수
# get을 사용하는 이유는 해당 키값에 대한 값이 존재하지 않을 때 None을 받기 위해서.
# print(phone['도우넛'])
print(phone.get('도우넛'))

# setDefault
# get 과 차이점은 실제로 데이터를 저장 한다.
print(phone.setdefault(('도우넛', '333-333-3333')))
print(phone)

# 삭제와 동시에 값 가져오기
number = phone.pop('둘리')
print(number)
print(phone)

# 튜플로 가져오기
item = phone.popitem()
print(item, type(item))
print(phone)

# 업데이트
phone.update({
    '도우넛': '1234-1234-1234',
    '또치': '444-4444-4444'
})
print(phone)

# 모두 삭제하기
phone.clear()
print(phone)
