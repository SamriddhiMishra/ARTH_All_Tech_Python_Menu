import os
os.system("yum install httpd")
os.system("cd /var/www/html ; echo YOU_ARE_CONFIGURED > fire.html")
os.system("systemctl start httpd")
os.system("systemctl enable httpd")

