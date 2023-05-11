import datetime

# 2023-04-27 15:21:39.851767 获取当前时间的字符串
print(datetime.datetime.now())

# 计算几天前或者几天后的时间
print(datetime.datetime.now()+datetime.timedelta(3)) # 3就是当前时间往后加3天  -3是往前3天 hours=3 三个小时之后的时间 mins是分钟

