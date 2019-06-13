# packing : tuple 만 가능하다.

t = 10, 20, 30, 'python'
print(t, type(t))

# unpacking
a, b, c, d = t
print(a, b, c, d)

# error  - > 튜플 개수에 맞춰 언패킹 작업이 진행되어야 한다.
# a, b, c = t
# print(a, b, c)

# unpacking extended
t = 1, 2, 3, 4, 5
a, *b, c, d = t
print(a, b, c, d)

a, b, *c = t
print(a, b, c)
a, *b, c = t
print(a, b, c)


# cf. 여러 파라미터를 받는 함수
def mysum(*num):
    sum = 0
    for n in num:
        sum += n
    return sum


print(mysum(1, 2))
print(mysum(1, 2, 3))
print(mysum(1, 2, 3, 4, 5, 6))


# c의 printf() 함수 흉내내기
def printf(s, *form):
   print(s % form)


printf("name : %s, age : %d", "둘리", 10)
