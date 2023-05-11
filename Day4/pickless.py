import pickle

info = {
    'name':'dsa',
    'age': 31
}

# 可以序列化所有数据类型   只能在python里使用pickle
f = open('test.txt','wb')
f.write(pickle.dumps(info))

#转换成二进制
print(pickle.dumps(info))

# 反序列化   如果有特殊的数据格式 比如函数也被序列化进了二进制数据中 反序列化的时候需要在程序里也有同名函数
# pickle.loads()

# 等同于f.write(pickle.dumps(info))
# pickle.dump(info,f)