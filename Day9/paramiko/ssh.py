import paramiko

privete_key = paramiko.RSAKey.from_private_key_file('./id_rsa_pub.txt')

#创建SSH实例
ssh = paramiko.SSHClient()

#允许链接不在know_hosts 文件中的主机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#链接服务器

# ssh.connect(hostname="localhost",port=22,username='root',password='root')
ssh.connect(hostname="localhost",port=22,username='root',pkey=privete_key)


#执行命令
stdin,stdout,stderr = ssh.exec_command('df')

#获取结果
res,err = stdout.read(),stderr.read()
result = res if res else err
print(result.decode())

#关闭
ssh.close()



#sftp

sftp_privete_key = paramiko.RSAKey.from_private_key_file('./id_rsa_pub.txt')
#创建类似scp功能的ssh
trp = paramiko.Transport(('hostname',22))
# trp.connect(username='root',password='root')
trp.connect(username='root',pkey=sftp_privete_key)

sftp = paramiko.SFTPClient.from_transport(trp)
#将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py','/tmp/test.py')
#将'remove_path'下载到本地'local_path'
sftp.get('remove_path','local_path')

trp.close()