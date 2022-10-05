money = True
if money : 
    print("택시를 타고 가라")
else:
    print("걸어가라")

x = 3
y = 2
print(x != y)   # x와 y는 같지 않다

money = 2000
if money < 3000:
    print("걸어가라")
else:
    print("택시를 타고 가라")

money = 2000
card = True
if money >= 3000 or card :
    print("택시를 타고 가라")
else : 
    print("걸어가라")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a','b','c'))

pocket = ('paper', 'smartphone', 'wallet', 'money')
if 'card' in pocket :
    print("버스를 타고 가라")
else:
    print("걸어가라")

if 'money' in pocket :
    pass                     # 아무런 일도 하지 않도록 설정하고 싶을 때 pass 사용
else :
    print("카드를 꺼내라")

if 'money' in pocket :
    print("택시를 타고 가라")
elif 'card' :
    print("버스를 타고 가라")
else :
    print("걸어가라")

# 조건부 표현식
score = 10
if score >= 60:
    message = "success"
else :
    message = "failure"

message = "success" if score >= 60 else "failure"   # 조건부 표현식(conditional expression  # 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우