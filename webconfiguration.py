import os

os.system ("tput setaf 2")
print("Here is web configuration")

choice=input("Enter 1 for web configuration ")
if choice=="1":

  os.system("yum install httpd")

  name=input("Enter your file name :")
  inp=input("Eenter here your file content : ")
  os.system("touch {}".format(name))
  os.system("echo '{}' > /var/www/html/{}".format(inp,name))
  os.system("systemctl start httpd")

  os.system("tput setaf 3")
  print("================== configuration done=======================")

