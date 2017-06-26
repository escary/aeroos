#!/usr/bin/python
#encoding: utf-8
import os, sys, subprocess, time


def reconocimiento():
  os.system("clear")
  z = raw_input("ingrese la ip ") 
  print "abra outra terminal porfavor e volte aqui\n"
  time.sleep( 1 )
  print " apos a carinha feliz e escreva ""killall ping""na outra terminal"
  time.sleep(0.5)
  print " :)"
  global real
  real = os.popen("ping "+z).read()
  return 
######   


if len(sys.argv) >= 2  :
  if sys.argv[1] in ("h", "help", "-h"):
    print "\nEste script procura saber informaçao via ping para obter o s.o em determinado host,para definir o host inicie o script ou escreva ""\n./aeroos.py ping ""'0.0.0.0'\n" 
    sys.exit()
#  elif sys.argv == "ping":
#    print "abra outra terminal"
#    time.sleep( 1 )
#    print "escreva 'killall ping' na terminal que vc abriu depois da carinha feliz"
#    time.sleep( 0.5 )
#    print ":)"
#    pass
  
   
else :
   reconocimiento()
   pass


#ip = sys.argv[3]
#w = open("ping.txt", "w+")
##w.write(str( ip ))
#w.close()
#w = open("ping.txt", "r+")
#read = w.read()


#real = os.popen("ping "+ read).read()
#print "analisando resultsados"
#time.sleep( 1 )

linux = real.find("64")
linux63 = real.find("63")
linux62 = real.find("62")
linux61 = real.find("61")
linux60 = real.find("60")
linux59 = real.find("59")
linux58 = real.find("58")
linux57 = real.find("57")
linux56 = real.find("56")
linux55 = real.find("55")
linux54 = real.find("54")
linux53 = real.find("53")
linux52 = real.find("52")
linux51 = real.find("51")
linux50 = real.find("50")
linux = (linux, linux63, linux62, linux61, linux60, linux59, linux58, linux57, linux56, linux55, linux54, linux53, linux52, linux51, linux50)

for i in linux:
 if i != -1:
  print "eh un sistema linux"
  break

 else :
    pass


windw128 = real.find("128")
windw127 = real.find("127")
windw126 = real.find("126")
windw125 = real.find("125")
windw124 = real.find("124")
windw123 = real.find("123")
windw122 = real.find("122")
windw121 = real.find("121")
windw120 = real.find("120")
windw119 = real.find("119")
windw118 = real.find("118")
windw117 = real.find("117")
windw116 = real.find("116")
windw115 = real.find("115")
windw114 = real.find("114")
windows = (windw128, windw127, windw126, windw125, windw124, windw123, windw122, windw121, windw120, windw119, windw118, windw117, windw116, windw115, windw114) 
for z in windows:
 vers0 = z
 
 if vers0 != -1: 
  print "possivel sistema windows"
  break
 else :
   pass 


unix = real.find("255")
unix254 = real.find("254")
unix253 = real.find("253")
unix252 = real.find("252")
unix251 = real.find("251")
unix250 = real.find("250")
unix249 = real.find("249")
unix248 = real.find("248")
unix = ( unix, unix254, unix253, unix252, unix251, unix250, unix249, unix248)
for q in unix:
   if q != -1:
     print "eh possivelmente um sistema unix"
     break
   else :
      pass 
if real.find("Host Unreachable") != -1:
   print "sistema inativo ou nao encontrado"



print "\npra ter mais informaçoes sobre o sistema use nmap ou um scanner metasploit"
opzoes = raw_input("quer mais info com respeito a fingerprint " )
if opzoes in ("si", "sim", "sii", "s", "S", "info", "ok") :

  print """para nmap use 
  nmap --sS -sV "ip" ou nmap -O "ip" 
  e outras opçoes dependendo do firewall e do host"""
  time.sleep( 0.8 )
  print "e pra metasploit podes usar um scanner da porta samba caso seja windows"
  
  time.sleep( 0.5 )
  print """exemplo
  auxiliary/scanner/smb/smb_version
  tmb tendo em conta que a porta smb precissa estar aberta
  assim podera obter info dos patch de segurança e tals"""


  print """
   licencia Copyleft(gnu GPL)
   para mais info leia o README.md
""" 



else : 
   print """
   licencia Copyleft(gnu GPL)
   para mais info leia README.md
"""
