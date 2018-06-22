mport paramiko

port=22
username='<usrname>'
password='<passwd>'

ip_list = ['blabla','blabla','blabla']


cmd='ls -l' 


ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for ip in ip_list:

	print("\n\non host : `%s`, for user: `%s`\n\n"%(ip,username))

	ssh.connect(ip,port,username,password)
	fileName = "./output/%s_output.txt"%(ip)
	file = open(fileName, 'w')

	stdin,stdout,stderr=ssh.exec_command(cmd)
	outlines=stdout.readlines()
	resp=''.join(outlines)
	print(resp)
	file.write(resp)

	file.close()


