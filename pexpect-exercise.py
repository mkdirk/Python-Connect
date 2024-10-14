import pexpect
import time
import os
from dotenv import load_dotenv

load_dotenv('../Python-Connect/venv/.env')
username = os.getenv('TELNET_USER')
passw = os.getenv('TELNET_PASSWORD')

ip_add = ["172.31.114.3", "172.31.114.4"]

for ip in ip_add:
    child = pexpect.spawn("telnet " + ip)
    child.expect('Username:')
    child.sendline(username)

    child.expect('Password:')
    child.sendline(passw)

    if ip == "172.31.114.3":
        child.expect('#')
        child.sendline('conf t')
        child.expect('#')
        child.sendline('int loopback0')
        child.expect('#')
        child.sendline('ip addr 172.16.1.1 255.255.255.255')
        time.sleep(2)
        child.close()
    else:
        child.expect('#')
        child.sendline('conf t')
        child.expect('#')
        child.sendline('int loopback0')
        child.expect('#')
        child.sendline('ip addr 172.16.2.2 255.255.255.255')
        time.sleep(2)
        child.close()
