##请打印一个类似下面的边长是n的直角三角形:
## *
## **
## *** 
## ****
# 提示: for i in range(m) 

def draw_triangle(n):
    for i in range(n):
        print((i+1) * "*")

draw_triangle(100)