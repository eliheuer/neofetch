#!/usr/local/bin/python3

import socket, platform
from os import system, remove

def local_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	return ip

def host_name():
	hostname = socket.gethostname()
	return hostname

def os_version():
	system("/usr/sbin/system_profiler SPSoftwareDataType | grep 'System Version' > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			os = info.strip()
			return os[16:30]

def model():
	system("/usr/sbin/system_profiler SPHardwareDataType | grep 'Model Identifier' > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			model = info.strip()
			return model[18:]

def screen_size():
	system("/usr/sbin/system_profiler SPDisplaysDataType |grep Resolution > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			size = info.strip()
			return size[12:]
def uptime():
	system("/usr/sbin/system_profiler SPSoftwareDataType | grep 'Time since boot:' > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			time = info.strip()
			return time[17:]
def shell():
	system("echo $SHELL > tmp.txt")
	#bash --version
	with open("tmp.txt", "r") as f:
		for info in f:
			shell = info.strip()
			return shell
def kernel():
	system("uname -a > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			kernel = info.strip()
			return kernel[61:67]

def cpu_spec():
	system("sysctl -n machdep.cpu.brand_string | grep Intel > tmp.txt")

	with open("tmp.txt", "r") as f:
		for info in f:
			cpu = info.strip().replace("CPU", "")	
			cpu_info = cpu.replace("  ", " ")
			return cpu_info

##########################
ip = local_ip()			 #
model = model() 		 #
os = os_version()	     #
size = screen_size() 	 #
uptime = uptime()	     #
shell = shell() 		 #
kernel = kernel() 		 #
hostname = host_name()	 #
cpu = cpu_spec() 		 #
##########################

print("\n"+"\033[92m                    'c.           "+str(hostname)+"\033[0m")
print("\033[92m                 ,xNMM.\033[0m"+"           " + "-" *len(hostname))
print("\033[92m               .OMMMMo\033[0m"+"\033[93m            OS\033[0m: " + str(os))
print("\033[92m               OMMM0,\033[0m"+"\033[93m             Kernel\033[0m: " + str(kernel))
print("\033[92m     .;loddo:' loolloddol;.\033[0m"+"\033[93m       Model\033[0m: " + str(model))
print("\033[92m   cKMMMMMMMMMMNWMMMMMMMMMM0:\033[0m"+"\033[93m     Shell\033[0m: " + str(shell))
print("\033[93m .KMMMMMMMMMMMMMMMMMMMMMMMWd.\033[0m"+"\033[93m     Uptime\033[0m: " + str(uptime))
print("\033[93m XMMMMMMMMMMMMMMMMMMMMMMMX.\033[0m"+"\033[93m       Resolution\033[0m: " + str(size))
print("\033[91m;MMMMMMMMMMMMMMMMMMMMMMMM:\033[0m"+"\033[93m        CPU\033[0m: " + str(cpu))
print("\033[91m:MMMMMMMMMMMMMMMMMMMMMMMM:\033[0m"+"\033[93m        IP\033[0m: " + str(ip))
print("\033[91m.MMMMMMMMMMMMMMMMMMMMMMMMX.\033[0m")
print("\033[91m kMMMMMMMMMMMMMMMMMMMMMMMMWd.\033[0m")
print("\033[95m .XMMMMMMMMMMMMMMMMMMMMMMMMMMk\033[0m")
print("\033[95m  .XMMMMMMMMMMMMMMMMMMMMMMMMK.\033[0m")
print("\033[94m    kMMMMMMMMMMMMMMMMMMMMMMd\033[0m")
print("\033[94m     ;KMMMMMMMWXXWMMMMMMMk.\033[0m")
print("\033[94m       .cooc,.    .,coo:.\033[0m")
print("\n                                  \033[30m███\033[0m"+"\033[91m███\033[0m"+"\033[92m███\033[0m"+"\033[93m███\033[0m"+"\033[94m███\033[0m"+"\033[95m███\033[0m"+"\033[96m███\033[0m"+"\033[97m███\033[0m")
system("rm -rf tmp.txt")