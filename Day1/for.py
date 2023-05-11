


num = int(input("num: "))

for i in range(10):
    print(i == num,i,num)
    if i == 11 :
        break

# for 执行完了走这里，如果break了就不走这里
else:
    print("for exit")

#0起始位置  10 最大，3步长，默认为1
for i in range(0,10,3):
    print(i == num,i,num)
    if i == 11 :
        break
    else:
        continue

# for 执行完了走这里，如果break了就不走这里
else:
    print("for exit")