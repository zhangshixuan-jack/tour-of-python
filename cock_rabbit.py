# 有n只鸡兔同在一个笼子里，从上面数，有35个头，从下面数，有94只脚。问笼中各有多少只鸡和兔？
## 常量 constants
cock_legs=2
rabbit_legs=4

def cock_and_rabbit(heads, legs):
    if heads < 0:
        print("头出错了！！！")
        return 0, 0
    if legs < 0 or legs % 2:
        print("腿出错了！！！")
        return 0, 0
    legs1 = heads*cock_legs # 如果都是鸡 总共有多少条腿
    legs2 = legs-legs1
    rabbits =  legs2/(rabbit_legs-cock_legs)
    cocks = heads-rabbits
    return rabbits, cocks

r, c = cock_and_rabbit(45, 100)

print("倒推法:鸡有%d只,兔子有%d只" % (c, r))


def cock_and_rabbit_1(heads, legs):
    for cock in reversed(range(0, heads+1)):
        cl = cock * cock_legs
        rabbits = heads - cock
        rabbit_legs = rabbits * 4
        if (cl + rabbit_legs) == legs:
            return rabbits, cock
    print("列举法:我算不出来!!!")
    return 0, 0

r, c = cock_and_rabbit_1(4500000, 10000000)

print("列举法:鸡有%d只,兔子有%d只" % (c, r))