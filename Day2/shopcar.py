


car = [
    ("IPhone 1","50000"),
    ("IPhone 2","51000"),
    ("IPhone 3","52000"),
    ("IPhone 4","53000"),
    ("IPhone 5","55000")
]

n = input("select product : ")

if n.isdigit() :
    n = int(n)
    while True :
        for i,p in enumerate(car):
            print(i,p)
            break
# print(car.index(p),p)
# if n == car.index(p):
#     break



