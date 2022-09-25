# 연관배열(Associative array), 해시(Hash) = 딕셔너리(Dictionary)
# {key : value}

a = {1 : 'hi'}
a = {'a' : [1,2,3]}

a = {1 : 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
del a[1]            # key가 1인 {key : value} 삭제
print(a)

# dictionary 에서 key 사용해 value 얻기
grade = {'JunYeong' : 3, 'JaeHyun' : 1}
print(grade['JunYeong'])                    # dictionary parameter name[Key]

print(grade.get('JunYeong'))       #get은 소괄호

a = {'a' : 1, 'b' : 2}
print(a['a'])

a = {'a' : 1, 'a' : 2}           # 중복 불가능
print(a)

a = {(1,2,3,4) : 2}        # key에 list는 불가능(변하는 자료형)

# dictionary 관련 함수
a = {'name' : 'JaeHyun', 'age' : 19, 'height' : 180, 'weight' : 80}
print(a.keys())            # key만 추출
print(list(a.keys()))

for k in a.keys():
        print(k)
for k in a.values():
        print(k)
for k in a.items():       # items() : 쌍 얻기
        print(k)

print(a.get('nokey'))     #None을 반환
print(a.get('foo', 'bar'))    # key가 dictionary에 없으면 default 값 반환
print('name' in a)
print(not 'name' in a)


        