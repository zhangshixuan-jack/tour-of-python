# 货运站运来36个大箱子,分别请9辆车来搬运,规定每辆车每次只能运4个箱子,请问这9辆车是否一次可以运完36个箱子?
boxes=36
trunks=9

if 4*trunks == boxes:
    print('yes')
else:
    print('no')

# 货运站运来n个大箱子,分别请m辆车来搬运,规定每辆车每次只能运4个箱子,请问这m辆车是否一次可以运完这些箱子?
def foo(boxes, trunks):
   if 4*trunks == boxes:
    print('yes')
   else:
    print('no')

foo(36, 9)
foo(72, 9)