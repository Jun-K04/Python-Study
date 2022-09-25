# set은 set keyword를 사용해 만든다.
s1 = set([1,2,3])
print(s1)

s2 = set("Hello")    # 중복 허용하지 않음 , 순서가 없다(unordered) : indexing 불가능
print(s2)

s1 = set([1,2,3])
l1 = list(s1)
print(l1)

t1 = tuple(s1)
print(t1)
print(t1[0])

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)                  # 교집합
print(s1.intersection(s2))

print(s1 | s2)                  # 합집합
print(s1.union(s2))

print(s1 - s2)                  # 차집합
print(s1.difference(s2))

# set 관련 함수
s1 = set([1,2,3])
s1.add(4)               # 값 1개 추가하기
print(s1)
s1.update([4,5,6])      # 값 여러개 추가하기
print(s1)
s1.remove(2)            # 특정 값 제거하기
print(s1)
