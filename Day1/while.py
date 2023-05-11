import getpass

num = int(getpass.getpass("num: "))

# True 必须大写的T
while num <= 10:
    print(num)
    num += 1

    # if num == 10:
    #     break
else:
    print("gt 10")
