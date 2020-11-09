import os

os.system("tput setaf 3")
print("\t\t\t Welcome to our Python Automation Menu")
os.system("tput setaf 7")
print("\t\t\t -------------------------------------------")

os.system("tput setaf 2")
print("Press 1 for Hadoop COnfiguration : ")
print("Press 2 for Data Upload and read from cluster FS : " )
print("Press 3 for Linux Partition Static : ")
print("Press 4 for LVM Partitions : ")
print("Press 5 for Linear Regression MOdel able to predict : ")
print("Press 6 for Configure webserver : ")
print("Press 7 for Creating webpages that auto host on webserver : ")
print("Press 8 for Launch AWS instance : ")

os.system("tput setaf 12")
print("\n")
choice=input("Enter your choice from 1 to 8 : ")

if choice == "8":
   keyname=input("Enter keyname ")
   y= os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
   os.system("tput setaf 3")
   os.system("---------launching instance------------")
   os.system("aws ec2 run-instances --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count 1 --subnet-id subnet-a6c8b7ea --security-group-ids sg-001d11f6401ccb83f --key-name {}".format(keyname))





