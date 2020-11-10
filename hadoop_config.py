import os
import subprocess as sp

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))



def hdfs(cmd):
	os.system(cmd+"cd /etc/hadoop ; rm hdfs-site.xml")
	os.system("touch hdfs-site.xml")
	f=open("hdfs-site.xml","w")
	f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/hadoop</value>
</property>
</configuration>""")
	f.close()
	os.system(cmd+"echo 3 > /proc/sys/vm/drop_caches")
def core(cmd,ip):
	os.system(cmd+"cd / ; rm -r hadoopnode -force")
	os.system(cmd+"mkdir /hadoopnode")
	prCyan("Folder Created with Name hadoop")
	os.system(cmd+"yum install wget -y")
	x=sp.getstatusoutput(cmd+"hadoop version")
	print(x)
	os.system(cmd+"wget http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm")
	os.system(cmd+"wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
	os.system(cmd+"rpm -ivh jdk-8u171-linux-x64.rpm")
	os.system(cmd+"rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
	os.system(cmd+"cd /etc/hadoop ; rm core-site.xml")
	os.system("touch core-site.xml")
	f=open("core-site.xml","w")
	f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!-- Put site-specific property overrides in this file. -->
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{0}:9001</value>
</property>
</configuration>""".format(ip))
	f.close()
	os.system(cmd+"cp core-site.xml /etc/hadoop/core-site.xml")
def hadoop_config():
	while True:
		os.system("clear")
		prRed("\n\n    ***** This is an automation script to configure nodes of HADOOP *****\n\n")
		prGreen("Enter \n 1. to configure this system \n 2. to configure another system(must have ssh access)\n\n          ")
		option1=int(input(""))
		if option1 == 1:
			cmd="sudo "
			os.system("clear")
			prYellow("Enter your option \n 1. Name Node \n 2. Data Node\n 3. Client\n")
			prYellow("Enter your choice")
			option2=int(input(""))
			if option2 == 1:
				os.system("clear")
				core(cmd,"0.0.0.0")
				prLightPurple("Done with core-site")
				hdfs(cmd)
				prLightPurple("Done with hdfs-site")
				os.system(cmd+"hadoop namenode -format -force")
				prLightPurple("*****NAME NODE FORMATTED*****")
				os.system(cmd+"hadoop-daemon.sh start namenode")
				os.system("clear")	
				prGreen(">>>>> NAME NODE STARTED <<<<<")
			elif option2 == 2:
				os.system("clear")
				prYellow("Enter the IP of the master     ")
				ip=input("")
				core(cmd,ip)
				prLightPurple("Done with core-site")
				hdfs(cmd)
				prLightPurple("Done with hdfs-site")
				os.system(cmd+"hadoop-daemon.sh start datanode")
				os.system("clear")
				prGreen(">>>> DATA NODE STARTED <<<<<")
			elif option2==3:
				os.system("clear")
				prYellow("Enter the IP of the master")
				ip=input("")
				core(cmd,ip)
				prLightPurple("Done with core-site")
				os.system(cmd+"hadoop-daemon.sh start client")
				prGreen(">>>>> CLIENT STARTED <<<<<")
		elif option1==2:
			os.system("clear")
			prYellow("Enter the username:     ")
			username=input("")
			prYellow("Enter the IP which you want to configure:     ")
			ipmain=input("")
			prYellow("Enter the keypair (eg /home/username/keyname.pem):     ")
			keyadd=input("")
			cmd="ssh -l {} {} -i {} sudo ".format(username,ipmain,keyadd)
			prYellow("Enter your option \n 1. Name Node \n 2. Data Node\n 3. Client\n")
			option2=int(input(""))
			if option2 == 1:
				os.system("clear")
				core(cmd,"0.0.0.0")
				os.system("scp -i {0} core-site.xml {1}@{2}:/home/{1}/core-site.xml".format(keyadd,username,ipmain))
				os.system(cmd+"cp core-site.xml /etc/hadoop/core-site.xml")
				prLightPurple("Done with core-site")
				hdfs(cmd)
				os.system("scp -i {0} hdfs-site.xml {1}@{2}:/home/{1}/hdfs-site.xml".format(keyadd,username,ipmain))
				os.system(cmd+"cp hdfs-site.xml /etc/hadoop/hdfs-site.xml")
				prLightPurple("Done with hdfs-site")
				os.system(cmd+"hadoop namenode -format -force")
				prLightPurple("*****NAME NODE FORMATTED*****")
				os.system(cmd+"hadoop-daemon.sh start namenode")
				prGreen(">>>>> NAME NODE STARTED <<<<<")
				os.system("jps")
			elif option2 == 2:
				os.system("clear")
				prYellow("Enter the IP of the master     ")
				ip=input("")
				core(cmd,ip)
				os.system("scp -i {0} core-site.xml {1}@{2}:/home/{1}/core-site.xml".format(keyadd,username,ipmain))
				os.system(cmd+"cp core-site.xml /etc/hadoop/core-site.xml")
				prLightPurple("Done with core-site")
				hdfs(cmd)
				os.system("scp -i {0} hdfs-site.xml {1}@{2}:/home/{1}/hdfs-site.xml".format(keyadd,username,ipmain))
				os.system(cmd+"cp hdfs-site.xml /etc/hadoop/hdfs-site.xml")
				prLightPurple("Done with hdfs-site")
				os.system(cmd+"hadoop-daemon.sh start datanode")
				prGreen(">>>> DATA NODE STARTED <<<<<")
			elif option2==3:
				prYellow("Enter the IP of the master")
				ip=input("")
				core(cmd,ip)
				prLightPurple("Done with core-site")
				os.system("clear")
				os.system(cmd+"hadoop-daemon.sh start client")
				prGreen(">>>>> CLIENT STARTED <<<<<")
