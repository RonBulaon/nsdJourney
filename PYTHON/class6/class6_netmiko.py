# Class 6 : CLI Automation with Python using netmiko
# Excercise by Ron Bulaon

from netmiko import ConnectHandler
from paramiko import HostKeys

sshCli = ConnectHandler(
    device_type='cisco_ios',
    host='10.128.207.132',
    port='22',
    username='cisco',
    password='cisco123!',
)

loopBack1 = [
    'int loopback 1', 
    'ip address 2.2.2.2 255.255.255.0', 
    'description WHATEVER'
    ] 

loopBack2 = [
    'int loopback 2', 
    'ip address 2.2.2.2 255.255.255.0', 
    'description NewButSame'
    ] 

def sendCommand(cmdType,cliCommand):
    global sshCli
    if cmdType == 'send_command':
        output = sshCli.send_command(cliCommand)
    if cmdType == 'send_config_set':
        output = sshCli.send_config_set(cliCommand)

    print("%s\n%s" % (cliCommand,output))
    return

cliCommand='show ip int brief'

sendCommand('send_config_set',loopBack1)
sendCommand('send_config_set',loopBack2)
sendCommand('send_command',cliCommand)
