def add(a,b) :
    return a + b
a = 4
b = 5
c = add(a, b)
print(c)

# 일반적인 함수
def add(a,b):
    result = a + b
    return result
a = add(3,4)
print(a)

# 입력값이 없는 함수
def say():
    return 'hi'
a = say()
print(a)

#결괏값이 없는 함수
def add(a,b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
a = add(3,4)          # <수행할 문장>을 출력
print(a)              # 결괏값은 없음

#입력값도 결괏값도 없는 함수
def say():
    print('Hi')
say()

#매개변수 지정하여 호출하기
def add(a,b):
    return a + b
result = add(b=3, a=8)
print(result)

#입력값의 개수를 모를 때
def add_many(*args):   # 입력값을 모두 tuple로
    result = 0
    for i in args:
        result += i
    return result
result = add_many(1,2,4,5,6,7,8,9)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result
result = add_mul("mul", 1,2,4,5,6)
print(result)
result = add_mul("add", 1,5,5,46)
print(result)

# keyword parameter      
def print_kwargs(**kwargs):        # 입력값을 모두 dictionary로 
    print(kwargs)                  # keyword arguments (kwargs)    
print_kwargs(a=1)
print_kwargs(name = 'foo', age = 3) # key = value 형태의 결괏값이 dict에 저장된다.

#함수의 결괏값은 하나이다.
def add_and_mul(a,b):
    return a+b, a*b       # tuple로 묶어 하나의 값으로 출력
print(add_and_mul(3,5))

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)
say_nick("바보")
say_nick("천재")

#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man = True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself('준영', 19)



