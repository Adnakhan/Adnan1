#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To shabirbaloch
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:B4_Baloch
##### LOGO #####
logo = """
      \033[1;91m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦТтЦТтЦТтЦИтЦИтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦИтЦИтЦИ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;92m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦТтЦТтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦТтЦТ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;93m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦТтЦТтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦИтЦИтЦТ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;94m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦТтЦТтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦИтЦТтЦТтЦТ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;95m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦИтЦИтЦИтЦТтЦИтЦИтЦИтЦТтЦТтЦИтЦТтЦТтЦИтЦИтЦИтЦИ  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд : 
      \033[1;96m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд      тЦЗЁЯД╡ЁЯД░ЁЯД▓ЁЯД┤ЁЯД▒ЁЯД╛ЁЯД╛ЁЯД║тЦЗ     тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;91m:  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд        тЦВтЦЗЁЯД║ЁЯД╕ЁЯД╜ЁЯД╢тЦЗтЦВ     тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд :
      \033[1;94m:  

  /$$$$$$        /$$                              
 /$$__  $$      | $$                              
| $$  \ $$  /$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$__  $$| $$__  $$ |____  $$| $$__  $$
| $$__  $$| $$  | $$| $$  \ $$  /$$$$$$$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$ /$$__  $$| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$| $$  | $$
|__/  |__/ \_______/|__/  |__/ \_______/|__/  |__/
                                                  
                                       Adnan           
                                                  

\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд\033[1;96mBalochhacker\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;93m                 тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд BalochHacker тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;93m                 тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  WhatsApp  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;93m                 тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд 03232132362тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд\033[1;96mBalochHacker\033[1;95mтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтАвтЧИтАвтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
  \033[1;96m          тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  тХ▒тЦФтЦФтЦФтЦФтХ▓  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд 
  \033[1;96m          тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦХтЦХтХ▓тФКтФКтХ▒тЦПтЦП тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
  \033[1;96m          тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд тЦХтЦХтЦВтХ▒тХ▓тЦВтЦПтЦП тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
 \033[1;96m           тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  тХ▓тФКтФКтФКтФКтХ▒  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
 \033[1;96m           тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  тЦХтХ▓тЦВтЦВтХ▒тЦП  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
 \033[1;96m           тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд  тХ▒тЦФтЦФтЦФтЦФтФКтФКтФКтФКтЦФтЦФтЦФтЦФтХ▓  тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
  \033[1;96m          тЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧдтЧетЧд
       \033[1;93m    тЦИтЦИтЦИтЦИтЦИтЦИтЦИтЦТтЦТWelcome To Adnan
