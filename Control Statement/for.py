""" for 변수 in list or tuple or 문자열
        수행할 문장1
        수행할 문장2"""

test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a :
    print(first + last)

score = [90, 25, 60, 76, 89]
number = 0
for a in score :
    number = number + 1
    if a < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

a = range(10)   # range(0, 10) = 0,1,2,3,4,5,6,7,8,9
print(a)

a = range(1, 11)
print(a)

add = 0
for i in range(1,11) :
    add = add + i
print(add)

marks = [90, 25, 67, 45, 80]
print(marks[0])
for i in range(len(marks)) :
    if marks[i] < 60:
        continue
    else :
        print("%d번 학생 축하합니다. 합격입니다." % (i +1) )

number = 0
for i in range(1, 101) :
    number = number + i
print(number)

for i in range(2, 10) :
    for j in range (1, 10) :
        print(i * j, end = " ")       # 매개변수 end는 결괏값을 출력할 때 다음 줄로 넘기지 않게 한다.
    print('')                         # print('')는 두 번째 for문이 끝나면 다음 줄부터 출력하게 해주는 문장이다.

# list comprehension(리스트 내포)
a = [1,2,3,4]
result = []
for num in a :
    result.append(num*3)
print(result)

result = [num*3 for num in a]        # list안에 for문을 사용
print(result)

result = [num *3 for num in a if num % 2 == 0]    # 짝수만 담기
print(result)

result = [x*y for x in range(2, 10)
              for y in range(1, 10)]
print(result)

#1
a = "Life is too short, you need python"

if "wife" in a : print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else: print("none")

#2
result = 0
i = 1
while i <= 1000 :     # while문으로 작성
    if i % 3 == 0 :
        result += i
    i += 1
print(result)

result = 0
for i in range(1,1001) :   # for문으로 작성
    if i % 3 == 0:
        result += i
print(result)

#3
i = 0     
while True:       # while문으로 작성
    i += 1     
    if i > 5 :
        break
    print("*"*i)

for i in range(1,6) :  # for문으로 작성
    print("*"*i)

#4
for i in range(1, 101) :
    print(i)

#5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / 10
print(average)

#6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers :
    if n % 2 == 1 :
        result.append(n*2)
print(result)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]  # list comprehension
print(result)


        