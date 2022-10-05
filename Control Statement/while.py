# 열 번 찍어 안 넘어가는 나무 없다
treeHit = 0
while treeHit < 10 :
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10 :
        print("나무 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4 :
    print(prompt)
    number = int(input())    # number가 4가 아닌 동안 prompt를 출력하고 사용자로부터 번호를 입력받는다.

# 커피 자판기
coffee = 10
while True :
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피 1캔이 나옵니다.")
        coffee = coffee - 1
    elif money > 300 :
        print("거스름돈 %d원을 주고 커피 1캔을 줍니다." % (money - 300))
        coffee = coffee - 1
        print("남은 커피 양은 %d개입니다." % coffee)
    else :
        print("돈이 부족합니다.")
        print("남은 커피 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
        break 

# while 문의 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

b = 0
while b <= 10:
    b = b + 1
    if b % 3 == 0: continue
    print(b)

# 무한 루프
""" while True :
        수행할 문장1
        수행할 문장2 ... """