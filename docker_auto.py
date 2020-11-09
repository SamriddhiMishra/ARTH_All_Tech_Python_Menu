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

def configureyum():
	os.system("clear")
	prPurple(">>>>>>>>>>>>>>  Configuring YUM  <<<<<<<<<<<<<<<")
	os.system("wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
	os.system("sudo rpm -ivh epel-release-latest-8.noarch.rpm")
	os.system("sudo yum install wget -y")
	os.system("sudo yum install -y yum-utils")
	prLightPurple("*****  DONE CONFIGURING YUM *****")

def configuredocker():
	os.system("clear")
	prPurple(">>>>>>>>>>>>>>  Configuring DOCKER  <<<<<<<<<<<<<<<")
	podman=sp.getstatusoutput("yum list installed podman.x86_64")
	#if(0 in podman):
	prRed("!!!!!! WARNING INSTALLED PROGRAM CAN CAUSE AN ERROR !!!!!! \n !!!!!!PRESS u TO UNINSTALL PROGRAM else press any other KEY !!!!!!")
	u=input("")
	if(u=="u"):
		os.system("yum remove podman.x86_64")
		os.system("yum remove buildah-1.11.6-7.module_el8.2.0+305+5e198a41.x86_64")
	os.system("yum install docker-ce --nobest")	
	prLightPurple("*****  DONE CONFIGURING DOCKER *****")
	
	
op1=""
while(op1!="e"):
	os.system("clear")
	prCyan("*****  Enter e to exit*****\n\n 1. to configure YUM \n 2. to configure DOCKER \n 3. START DOCKER SERVICE \n 4. START DOCKER SERVICE PERMANENTLY \n 5. SEE DOCKER STATUS\n 6. USE DOCKER\n ")
	op1=input("")

	if op1 == "1":
		configureyum()
	elif op1 == "2":
		configuredocker()
	elif op1 =="3":
		os.system("sudo systemctl start docker")
	elif op1 == "4":
		os.system("sudo systemctl enable docker")
	elif op1 == "5":
		os.system("sudo systemctl status docker")
	elif op1 == "6":
		os.system("clear")
		op2=op1
		while(op2!="p"):
			prCyan("***ENTER p for Previous Menu***\n1. List all containers\n2. List all Images\n3. Pull an Image\n4. Launch a Container\n5. Delete a Container\n6. Delete all OS at once")
			op2=input("")
			if op2=="1":
				os.system("clear")
				os.system("docker ps")
			elif op2=="2":
				os.system("clear")
				os.system("docker images -a")
			elif op2=="3":
				op3=op2
				while(op3!="d"):
					os.system("clear")
					prPurple("Enter d for previous Menu\n\n*** OPTION *** \n1. Ubuntu\n2. CentOS\n3. WordPress\n4. MySQL\n5. Django\n6. Mongo")
					op3=input("")
					if op3=="1":
						os.system("docker pull ubuntu")
					elif op3=="2":
						os.system("docker pull centos")
					elif op3=="3":
						os.system("docker pull wordpress")
					elif op3=="4":
						os.system("docker pull mysql")
					elif op3=="5":
						os.system("docker pull django")
					elif op3=="6":
						os.system("docker pull mongo")
			elif op2=="4":
				os.system("clear")
				prPurple("Here is the list of the of OS available")
				os.system("docker images -a")
				prYellow("Enter the OS eg centos")
				osname=input("")
				prYellow("Enter the name of the container")
				name=input("")
				os.system("docker run -it --name {} {}".format(name,osname))
				
			elif op2=="5":
				prYellow("Enter the OS name")
				name=input("")
				os.system("docker rm {0}".format(name))
			elif op2=="6":
				os.system("docker rm `docker ps -a -q`")
	#elif op=="1":
		