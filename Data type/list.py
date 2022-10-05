# list는 대괄호 
odd = [1, 3, 5, 7, 9]

a = []
b = ["Life", "is", "too", "short"]
c = [1,3, "Junyeong"]                    #list 안에는 어떤 자료형이든지 가능하다

a= [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[3])
print(a[-1][0])            #list 안의 list에서 요소값 추출하기

a = [1, 2, ['a','b', ['Life', 'is']]]   # 심층 구조의 list
print(a[2][2][0])    

# list 의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])

b = a[:2]
print(b)

# list 연산하기
a = [1, 2 ,3]
b = [4, 5, 6]
print(a*3)
print(a+b)
print(len(a+b))
print(str(a[2]) + "hamburgers")      # int + string 의 연산은 불가하다.

# list의 수정과 삭제
a = [1, 2, 3]
a[1] = 4
print(a[1])
print(a)

del a[1:]           # del a[x] 는 x번째 요솟값을 삭제한다.
print(a)

# list 관련 함수
a = [1, 2, 3]
a.append(4)          # list의 맨 마지막에 4를 추가
print(a)
a.append([5,6])
print(a)

a = [1, 4, 3, 2]
a.sort()             # list의 요소를 순서대로 정리
print(a)

a = ['a', 's', 'm']
a.sort()
print(a)

a = ['a', 'c', 'b']
a.reverse()          # list의 순서를 거꾸로 뒤집는다.
print(a)

a = [1, 2, 3]
print(a.index(3))    #index(x) 에서 x의 위치 값을 돌려준다. 3은 a[2]이다.

a = [1, 2, 3]
a.insert(0, 4)       #insert(a,b)는 list의 a번째 위치에 b를 삽입한다.
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)          #remove(x)는 첫 번째로 나오는 x를 삭제한다.
print(a)

a = [1, 2, 3]
print(a.pop())       #pop(x)은 list의 x번째 요소를 돌려주고 그 요소는 삭제한다.
print(a)
print(a.pop(1))
print(a)

a = [1, 2, 3, 1]
print(a.count(1))   #connt(x)는 list 안에 x가 몇 개 있는지 알려준다.

a = [1, 2, 3]
a.extend([4, 5])    #extend(x)에서 x는 list만 올 수 있으며 원래의 a 리스트에 x 리스트를 더한다.
print(a)
b = [6, 7]
a.extend(b)
print(a) 

a += [4,5]          #a.extend(x) = a +=x 
print(a)            #'+='는 계산한 값을 원래 값에 할당한다고 해서 할당 연산자라 한다. 즉, i += 1은 i = i + 1과 같다.