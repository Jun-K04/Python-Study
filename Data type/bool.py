# bool은 True와 False를 나타내는 자료형
a = True
b = False
print(type(a))
print(type(b))

print(1==1)

a = [1, 2, 3, 4]
while a:
    print(a.pop())
print(a)

if []:
    print("참")
else:
    print("거짓")

# bool 연산
print(bool('python'))
print(bool(''))
print(bool(2))
print(bool(0))