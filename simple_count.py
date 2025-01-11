#数一数10000000以为有多少个数可以被53整除?
t = 0
for i in range(0,100000):
  if (i + 1) % 53 ==0:
    t = t + 1
    print((i + 1))
print(t) 
