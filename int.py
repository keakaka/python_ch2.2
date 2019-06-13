a = 23
print(a, type(a))
print(isinstance(a, int))

# 2진, 10진, 16진, 8진 상수(literal)

b = 0b1101
c = 0o23
d = 0x23
print(b, c, d)

# 3.x부터 int가 long과 합쳐졌다. (무한대 표현범위)
e = 2 ** 1024
print(e, type(e))

# 변환 변수
print(oct(38))
print(hex(38))
print(bin(38))

