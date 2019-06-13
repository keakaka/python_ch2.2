#

s = {1,2,3}
print(s, type(s))

s.add(2)
print(s)

s.discard(2)
print(s)

s.discard(2)
print(s)

# s.remove(2) # remove 는 없는 객체 제거 시 예외 발생
print(s)

s.update({2, 7, 8})
print(s)

s.clear()
print(s)

# 수학 집합 관련 객체함수
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}
s3 = s1.union(s2)
print(s3)

s3 = s1.intersection(s2)
print(s3)

s3 = s1.difference(s2)
print(s3)

s3 = s1.symmetric_difference(s2)
print(s3)

# print(s1.issuperset(s3))
# print(s3.issuperset(s1))

