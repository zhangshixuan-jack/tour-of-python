## 商场打折:
# 变形金刚商场搞促销活动,一个变形金刚50元,客户可以选择两种优惠方式之一:
# 1. 买2个送一个
# 2. 满300元减120元
# 现在jack想买n个变形金刚,请问用最少花多少钱?

def money(n):
    # 第一步 算第一种
    x1 = op1(n)

    #第二步 算第二种
    x2= op2(n)

    #第三步 比较并且返回小的那个数
    if x1>x2:
        return x2 
    else:
        return x1 

def op1(n):
    count = n / 3
    left = n % 3
    return (2 * count + left) * 50

def op2(n):
    total = 50 * n
    count = int(total / 300)

    return total - count * 120


print("买0个最少需要:", money(0))
print("买100个最少需要:", money(100))
