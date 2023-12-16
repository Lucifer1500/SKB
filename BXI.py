import os,platform
os.system('xdg-open https://www.facebook.com/AungZinMin.2006')
os.system('pip uninstall requests')
os.system('pip install requests')


print('username is:\033[0;92mBMH1')
import getpass

attemps = 0

while attemps < 12345677901:
    username = input(' \033[0;92mEnter Username: ')
    

    if username == 'BMH1' :
        print(' \033[0;92mYou Have Successfully Logged in.')
        break
    else:
        print(' Incorrect username Please Trying ')
        attemps += 1
        continue


BXI=platform.architecture()[0]
if BXI=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif BXI=="64bit":
    __import__("Proof")
