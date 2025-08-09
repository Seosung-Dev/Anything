import turtle as t
def value():
    global small, normal, smallcolor, normalcolor, big, bigcolor
    small = int(input("안 쪽에있는 꽃의 꽃잎 수를 지정하시오(360의 약수) : "))
    smallcolor = input("안 쪽에 있는 꽃의 색깔을 지정하시오(영어, 소문자) : ")
    normal = int(input("가운데에 있는 꽃의 꽃잎 수를 지정하시오(360의 약수) : "))
    normalcolor = input("가운데에 있는 꽃의 색깔을 지정하시오(영어, 소문자) : ")
    big = int(input("밖에 있는 꽃의 꽃잎 수를 지정하시오(360의 약수) : "))
    bigcolor = input("밖에 있는 꽃의 꽃잎의 색깔을 지정하시오(영어, 소문자) : ")
    return small, normal, smallcolor, normalcolor, big, bigcolor
def small_flower():
    global small, smallcolor
    t.speed(0)
    t.color(smallcolor)
    for i in range(small):
        for j in range(2):
            for k in range(100):
                t.forward(1)
                t.right(0.7)
            t.right(110)
        t.right(int(360/small))
def normal_flower():
    global normal, normalcolor
    t.color(normalcolor)
    for i in range(normal):
        for j in range(2):
            for k in range(100):
                t.forward(1.5)
                t.right(0.7)
            t.right(110)
        t.right(int(360/normal))
def big_flower():
    global big, bigcolor
    t.color(bigcolor)
    for i in range(big):
        for j in range(2):
            for k in range(100):
                t.forward(2)
                t.right(0.7)
            t.right(110)
        t.right(int(360/big))
def main():
    value()
    small_flower()
    normal_flower()
    big_flower()
    t.mainloop()
main()        
