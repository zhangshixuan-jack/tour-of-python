## 阅读下面的代码，看看它的作用是什么
# results = []

# for i in range(0,200):
#   if i % 3 == 0 and i % 7 == 0:
#     results.append(i)

# print(results)

#打印出5到99之间所有的偶数
q = 0
for i in range(5,100):
  if i % 2 == 0:
    print(i)
    q += 1     
print(q)     
