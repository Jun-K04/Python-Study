# 문자열 자료형
# multistringl.py

print("=" * 50)
print("My Program")
print("=" * 50)

multiline = "Life is too short\nYou need python"
print(multiline)

a = "blue jeans"
print(len(a))  # 문자열 길이 구하기
print(a[3])    # 앞에서부터 세어 4번째 문자
print(a[-2])   # 뒤에서부터 세어 첫 번째가 되는 문자

print(a[0:4])  # a[시작번호:끝번호] : 0<= a < 3
print(a[0:6])  # 공백도 포함하여 센다
print(a[6:])
print(a[4:-1])

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

b = "Pithon"
print(b[:1])
print(b[2:])
print(b[:1] + 'y' + b[2:]) # Pithon 을 Python 으로 

#포맷팅 
print("I eat %d apples"%3)
print("I eat %s apples"%"five") # %s는 모든 것 반환가능

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days."% (number, day))
print("Error is %d%%."%98)

print("%10s" % "hi")         #길이 10인 문자열 오른쪽정렬하고 나머지는 공백
print("%-10sjane."% 'hi')    #위와 동일, but 왼쪽정렬
print("%.4f" % 3.42135)      #소수점 표현하기
print("%10.5f" % 3.42135)

#format 함수 포맷팅
print("I eat {0} apples.".format(5))
print("I eat {0} apples.".format("five"))

number = 10
day = "three"
print("I ate {0} apples. While {1} days.".format(number, day))
print("I ate {number} apples.".format(number = 10))

print("{0:<10}".format("hi"))    #왼쪽 정렬, 총 자릿수 10
print("{0:>10}".format("hi"))    #오른쪽 정렬, 총 자릿수 10
print("{0:^10}".format("hi"))    #가운데 정렬
print("{0:!<10}".format("hi"))   #문자로 채우기

y = 3.141592
print("{0:0.4f}".format(y))

#f 문자열 포맷팅
name = "홍길동"
age = 30
print(f'나의 이름은 {name} 입니다.\n나이는 {age}입니다.')
print(f'나는 내년이면 {age+1} 살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'제 이름은 {d["name"]}입니다.\n나이는 {d["age"]}입니다.')

#문자열의 내장 함수
a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))                 #b가 처음 나온 위치
print(a.index('b'))                #존재하지 않는 문자를 찾으면 오류발생

print(",".join('abcd'))            # , 삽입

a= "hi"
print(a.upper())                   # 대문자로 바꾸기

a= "HI"
print(a.lower())                   # 소문자로 바꾸기

a = " hi "
print(a.lstrip())                  # 왼쪽 공백 지우기
print(a.rstrip())                  # 오른쪽 공백 지우기
print(a.strip())                   # 양쪽 공백 지우기

a = "Life is too short"
print(a.replace("Life", "Your leg")) # 문자열 바꾸기
print(a.split())            #공백을 기준으로 문자열 나누기

b = "a:b:c:d"
print(b.split(':'))         # ':' 을 기준으로 문자열 나누기

temperature = 18
print("현재 온도는 %d도 입니다." % temperature)

temperature = 35
print("오늘 최고기온은 %s도 입니다." % temperature)