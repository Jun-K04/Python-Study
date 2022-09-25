# 변수 = 객체
a = [1, 2, 3]
print(id(a))

b = a
print(id(b))
print(a is b)

# b 변수 생성할 떄 a와 다른 주소를 가리키는법
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy
a = [1, 2, 3]
b = copy(a)     # copy(a) = a[:]
print(a)
print(b)
print(a is b)

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
[a,b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a, b = b, a      # 두 변수의 값 바꾸기
print(a)
print(b)


# 연습문제
#1
score = {'국어': 80, '영어': 75, '수학': 55}
average =( score['국어'] + score['영어'] + score['수학'] ) / 3
print(average) 

#2
number = 13
if number % 2 == 1 :
    print("{0}은 홀수입니다.".format(number))
else :
    print("{0}은 짝수입니다.".format(number))

#3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#4
pin = "881120-1068234"
print(pin[7])

#5
a = 'a:b:c:d'
b = a.replace(":", "#")
print(b)

#6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

#7 
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#8
a = (1, 2, 3)
a = a + (4,)   # 한 개의 요소 쓸 때는 콤마
print(a)

#9
a = dict()
print(a)   # key에 list는 불가능

#10
a = {'A': 90, 'B': 80, 'C': 70}
result =a.pop('B')
print(a)
print(result)

#11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
print(aSet)
b = list(aSet)
print(b)

#12
a = b = [1, 2, 3]
a[1] = 4
print(b)