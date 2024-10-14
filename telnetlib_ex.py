import telnetlib
import time
import os
from dotenv import load_dotenv

load_dotenv('../Python-Connect/venv/.env')

user = os.getenv('TELNET_USER')
passw = os.getenv('TELNET_PASSWORD')

tn = telnetlib.Telnet("172.31.114.3")

tn.read_until(b"Username:")
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password:")
tn.write(passw.encode('ascii') + b"\n")

tn.write(b'conf t\n')
tn.write(b'int g0/1\n')
tn.write(b'vrf forwarding control-data\n')
tn.write(b'ip addr 192.168.1.1 255.255.255.0\n')
tn.write(b'no shut\n')
tn.write(b'exit\n')

tn.write(b'conf t\n')
tn.write(b'int g0/2\n')
tn.write(b'vrf forwarding control-data\n')
tn.write(b'ip addr 192.168.2.1 255.255.255.0\n')
tn.write(b'no shut\n')
tn.write(b'exit\n')

tn.close()