import random

# 密码生成
password = ''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%'
for i in range(16):
    password += random.choice(chars)

# 信息收集
info_site = input('What is the password for? (Enter website)\n')
info_name = input('What is your username for this website?\n')
info_contact = input('What is the e-mail/phone number you used for this website?\n')

# 信息存储
with open('password-collection.txt', 'at') as f:
    f.writelines("Website: "+info_site)
    f.writelines("\nUsername: "+info_name)
    f.writelines("\nE-mail/phone number: "+info_contact)
    f.writelines("\nPassword: "+password+"\n\n")

# 打印密码
print("The password is:"+password)
