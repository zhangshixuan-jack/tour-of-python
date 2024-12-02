##请打印一个类似下面的边长是n的直角三角形:
## *
## **
## *** 
## ****
# 提示: for i in range(m) 

def draw_triangle(n):
    for i in range(n):
        print((i+1) * "*")

#draw_triangle(100)

##请打印一个类似下面的n行的三角形:
##     *
##    *** 
##   *****
##  *******
def draw_triangle2(x):
    for i in range(x):
      print((2 * (i+1) - 1)*"*")

draw_triangle2(6)
  