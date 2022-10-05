print("Life""is""too""short")
print("Life", "is", "too short")

for i in range(10):
    print(i, end=' ')

result = 0
def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result
cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(5))

# 사칙연산 클래스
class FourCal:
    def setdata(self, first, second):     # 클래스 내부 함수는 메서드
        self.first = first
        self.second = second
a = FourCal()
a.setdata(4, 3)
print(a.first)

b = FourCal()
b.setdata(5, 7)
print(b.first)

id(a.first)
id(b.first)

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result 
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

# 생성자(Constructor)    객체에 초깃값 설정 / 객체가 생성될 때 자동으로 호출되는 메서드
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result 
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.first)
print(a.mul())

# 클래스의 상속
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4, 3)
print(a.pow())

class SafeFourCal(FourCal):
    def div(self):               #메서드 오버라이딩(덮어쓰기)
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(5, 0)
print(a.div())

# 클래스 변수
class Family:
    lastname = "김"

print(Family.lastname)
a = Family()
print(a.lastname)
print(id(Family.lastname))
print(id(a.lastname))

