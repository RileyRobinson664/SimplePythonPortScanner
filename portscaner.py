#Import our needed code
import socket
import subprocess
import sys 
#This is imported so that we can have the script tell us how long it took to run
from datetime import datetime

#Clears your screen
subprocess.call('clear', shell=True)

#Ask for a target IP address
remoteServer = input("Enter a IP address to scan: ")
remoteServerIP = socket.gethostbyname (remoteServer)

#Print a bannder with information on the ongoing scan
print ("_" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("_" * 60)

#Take note of date and time when the scan started
t1 = datetime.now()

#Use the range finction to specify ports. We will also do error handeling here.

try:
	for port in range (1, 5000):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print ("Port {}:      Open" .format(port))
		sock.close()
		
except KeyboardInterrupt:
	print ("Programed stopped.")
	sys.exit()

except socket.gaierror:
	print ("Hostname not found.")
	sys.exit()
	
except socket.error:
	print ("Conection failed.")
	sys.exit()
	
#Now we check the time again
t2 = datetime.now()

#Now we can calculate the diffrance between t1 and t2
total = t2 - t1

#Finaly we print the infomation
print ('Scanning Finished in: ', total)
