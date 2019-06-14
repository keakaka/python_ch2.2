
results = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = n * n
    results.append(result)

print(results)

# list comprehension
results = [n*n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(results)

# 문자열 리스트에서 길이가 2 이하인 문자열 List or Set
strings = ['a', 'as', 'as', 'bar', 'car', 'dove', 'python']
results = [s for s in strings if len(s) <= 2]
resultset = {s for s in strings if len(s) <= 2}
print(results)
print(resultset)

# 1 ~ 100 사이의 수 중에서 짝수 리스트
results = [i for i in range(1, 100) if i&1 == 0]
print(results)

# 문자열 길이를 set으로 저장하기
strings = ['a', 'as', 'as', 'bar', 'car', 'dove', 'python']
strlength = {len(s) for s in strings}
print(strlength)

# dict comprehension
strings = ['a', 'as', 'bar', 'car', 'dove', 'python']
d = {s: len(s) for s in strings}
print(d)

l = [n for n in range(1, 100)
     if '3' in str(n) and print(n, '짝')
     or '6' in str(n) and print(n, '짝')
     or '9' in str(n) and print(n, '짝')]
