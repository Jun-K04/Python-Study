# tuple 은 소괄호
t1 = ()
t2 = (1, 2, 3)
t3 = ('a', 'b', ('ab'))
t4 = (1,)                  # 1개의 요소 쓸땐 콤마
t5 = 1, 2, 3               # 괄호 생략 가능
print(type(t5))

t1 = (1, 2, 'a', 'b')      # 변화 불가능하다는 것만 빼면 성질은 list와 동일
t2 = 3, 4
print(t1[0])
print(t1[1:])
print(t1 + t2)
print(t2 * 3)
print(len(t1))


