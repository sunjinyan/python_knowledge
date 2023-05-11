import time

# Unix时间戳  就是Unix诞生时间
print(time.time())

# time.struct_time(tm_year=2023, tm_mon=4, tm_mday=27, tm_hour=14, tm_min=21, tm_sec=32, tm_wday=3, tm_yday=117, tm_isdst=0)
# tm_wday 一周的第几天 从0开始3代表第四天
# tm_yday 一年的第几天
# tm_isdst  DST 是否是夏令时 0 代表否    英国本初子午线:UTC格林尼治时间  中国是东八区:UTC+8 比标准时间早8个小时的意思  新疆是东五区:UTC+5
print(time.localtime(time.time()).tm_year) #struct  tuple

# 时区 中国在标准时间的东八区 所以是-8
print(time.timezone)
print(time.timezone/3600)

# time.sleep()

# 转换为struct time tuple 默认转换为UTC时间元组  使用的是当前时间time.time()
print(time.gmtime())

# 将时间的元组形式转换成时间戳
print(time.mktime(time.localtime()))

# 将时间元组形式转换成 string
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 将string转换成时间元组形式
print(time.strptime("2023-04-27 15:08:20","%Y-%m-%d %H:%M:%S"))


#Thu Apr 27 15:14:59 2023 将tuple 转换成 这样简化的字符串
print(time.asctime(time.localtime()))

#Thu Apr 27 15:17:23 2023  将时间戳转换成 这样简化的字符串
print(time.ctime(time.time()))