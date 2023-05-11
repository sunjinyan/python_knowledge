import shutil

# shutil.copyfileobj() 将文件内容 拷贝到另一个文件中 可以是部分内容


# shutil.copyfile() 给个文件名  然后读取内容 写入到另一个文件名中 权限等信息没有copy

# shutil.copymode() 只是copy 文件的权限给另外一个文件 只copy权限  内容、组、用户不变


# shutil.copystat()  copy所有信息  、权限等  没有赋值文件

# shutil.copy() 文件和权限都copy
# shutil.copy2() 文件和状态、权限信息都copy


# shutil.copytree() 递归拷贝文件到目标目录

# shutil.rmtree() 递归删除

# shutil.move() 移动文件


'''创建压缩包并返回文件路径，例如：zip、tar

创建压缩包并返回文件路径，例如：zip、tar

base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
如 data_bak                       =>保存至当前路径
如：/tmp/data_bak =>保存至/tmp/
format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir： 要压缩的文件夹路径（默认当前目录）
owner： 用户，默认当前用户
group： 组，默认当前组
logger： 用于记录日志，通常是logging.Logger对象


#将 /data 下的文件打包放置当前程序目录
import shutil
ret = shutil.make_archive("data_bak", 'gztar', root_dir='/data')
   
#将 /data下的文件打包放置 /tmp/目录
import shutil
ret = shutil.make_archive("/tmp/data_bak", 'gztar', root_dir='/data') 
'''
# shutil.make_archive()




'''
import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall(path='.')
z.close()
'''

'''
import tarfile

# 压缩
>>> t=tarfile.open('/tmp/egon.tar','w')
>>> t.add('/test1/a.py',arcname='a.bak')
>>> t.add('/test1/b.py',arcname='b.bak')
>>> t.close()


# 解压
>>> t=tarfile.open('/tmp/egon.tar','r')
>>> t.extractall('/egon')
>>> t.close()
'''