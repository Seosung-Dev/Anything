import turtle as t
import random
def valuable(): #변수를 지정합니다.
    global x, y, m1, m2, m3, m4, max1, max2, max3, max4, c1, c2, c3, c4, line
    x = 0
    y = 0
    m1 = 0 #제1 사분면
    m2 = 0 
    m3 = 0 
    m4 = 0
    max1 = 0 #연속으로 제1사분면이 나온 횟수
    max2 = 0 
    max3 = 0 
    max4 = 0
    c1 = 0 #제1 사분면에 들어온 횟수
    c2 = 0 
    c3 = 0 
    c4 = 0
    line = 0 #선에 겹쳤을 때를 카운트하기 위한 변수
def draw_prime():
    t.shape("circle") #터틀의 모양을 원으로 설정합니다.
    t.shapesize(0.2) #터틀의 크기를 알맞게 조정합니다.
    t.speed(0)
    t.goto(-500, 0)
    t.goto(-500, -500)
    t.goto(500, -500)
    t.goto(500, 500)
    t.goto(-500, 500)
    t.goto(-500, 0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(0,500)
    t.goto(0, -500)
    t.goto(0, 0)
    t.goto(500, 0)
    t.goto(-500, 0)
def draw_random_point(): #랜덤한 점을 그립니다.
    global x, y, m1, m2, m3, m4, max1, max2, max3, max4, c1, c2, c3, c4, line
    x = random.randint(-500, 500) #x좌표를 랜덤으로 설정합니다.
    y = random.randint(-500, 500)
    if x > 0 and y > 0:
        m1 += 1
        m2, m3, m4 = 0, 0, 0 #제1 사분면에 들어오면 다른 사분면의 카운트를 초기화합니다.
        if m1 > max1: #제1 사분면이 연속으로 나온 횟수가 최대값보다 크면 최대값을 갱신합니다.
            max1 = m1
        c1 += 1 #제1 사분면에 들어온 횟수를 카운트합니다.
    elif x < 0 and y > 0:
        m2 += 1
        m1, m3, m4 = 0, 0, 0
        if m2 > max2:
            max2 = m2
        c2 += 1
    elif x < 0 and y < 0:
        m3 += 1
        m1, m2, m4 = 0, 0, 0
        if m3 > max3:
            max3 = m3
        c3 += 1
    elif x > 0 and y < 0:
        m4 += 1
        m1, m2, m3 = 0, 0, 0
        if m4 > max4:
            max4 = m4
        c4 += 1
    if x == 0 or y == 0:
        line += 1
    t.penup()
    t.goto(x, y)
    t.stamp()
def main():
    valuable()
    draw_prime()
    a = int(input("반복할 횟수를 적어주세요 : "))
    for i in range(a):
        draw_random_point()
    print("제1 사분면에 들어온 횟수 : ", c1)
    print("제2 사분면에 들어온 횟수 : ", c2)
    print("제3 사분면에 들어온 횟수 : ", c3)
    print("제4 사분면에 들어온 횟수 : ", c4)
    print("제1 사분면이 연속으로 나온 횟수 : ", max1)
    print("제2 사분면이 연속으로 나온 횟수 : ", max2)
    print("제3 사분면이 연속으로 나온 횟수 : ", max3)
    print("제4 사분면이 연속으로 나온 횟수 : ", max4)
    print("선에 겹친 횟수 : ", line)
    t.mainloop() #터틀을 유지합니다.
main()