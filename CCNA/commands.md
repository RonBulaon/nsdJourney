<!-- TOC -->

- [CCNA I : Introduction to Networks](#ccna-i--introduction-to-networks)
  - [Global Commands](#global-commands)
  - [Secure Management Access](#secure-management-access)
  - [IP Addressing Switch](#ip-addressing-switch)
  - [Switch Port](#switch-port)
  - [VLANs](#vlans)
  - [Router](#router)
  - [Routing](#routing)
  - [Dynamic Routing](#dynamic-routing)
  - [IPv6 Commands](#ipv6-commands)
  - [Basic Router Security](#basic-router-security)
  - [Sample Command Sequence](#sample-command-sequence)
    - [Switch](#switch)
    - [Router](#router-1)
    - [Case Study : CCNA Level 1](#case-study--ccna-level-1)
      - [Host Side Configuration](#host-side-configuration)
      - [Router Side Configuration](#router-side-configuration)
      - [Switch Side Configuration](#switch-side-configuration)
      - [Other Commands](#other-commands)
- [CCNA II : Switching, Routing, and Wireless Essentials](#ccna-ii--switching-routing-and-wireless-essentials)
  - [Switch SVI Configuration Example](#switch-svi-configuration-example)
  - [VLAN Configuration](#vlan-configuration)
  - [Configure Trunks](#configure-trunks)
  - [Dynamic Trunking Protocol(DTP)](#dynamic-trunking-protocoldtp)
  - [802.1Q Encapsulation](#8021q-encapsulation)
  - [Activity : Configure Layer 3 Switching and Inter-VLAN Routing](#activity--configure-layer-3-switching-and-inter-vlan-routing)
    - [Part 1 : Configure Layer 3 Switching](#part-1--configure-layer-3-switching)
    - [Part 2 : Configure Inter-VLAN Routing](#part-2--configure-inter-vlan-routing)
    - [Part 3 : Configure IPv6 Inter-VLAN Routing](#part-3--configure-ipv6-inter-vlan-routing)

<!-- /TOC -->

[Back to README](../README.md)

<br/><br/>

# CCNA I : Introduction to Networks
## Global Commands
* Go to configuration mode
    ```bash
    Switch> enable
    Switch# config terminal
    Switch(config)# 
    ```
* Configure Hostname
    ```bash
    Switch> enable
    Switch# config terminal
    Switch(config)# hostname newSwitchHostname
    newSwitchHostname(config)#
    ```
* Disable IP Domain Lookup
    ```bash
    Switch(config) #no ip domain-lookup
    ```
* Create a banner message
    ```bash
    Switch(config)# banner motd #Authorized access only!#
    ```
* copy running config to start up file
    ```bash
    Switch(config) #copy running-config startup-config
    ```
* Show Running/Startup Configuration
    ```bash
    Switch(config) #show running-config
    Switch(config) #show startup-config
    ```
* All info about the device, OS, interfaces, size of flash memory etc.
    ```bash
    Switch# show version 
    ```
* show contents of flash memory 
    ```bash
    Switch# show flash
    ```
 * Reset switch to factory default. delete startup-config and vlan.dat
    ```bash
    Switch# erase startup-config 
    Switch# delete flash:vlan.dat
    Switch# show flash
    Switch# show start
    Switch# reload
    ```
 [Back to Top](#cisco-cli-commands)

## Secure Management Access
* Secure console lines
    ```bash
    Switch(config)# line console 0
    Switch(config-line)# password <password>
    Switch(config-line)# login
    Switch(config-line)# exit
    ```
* Secure VTY lines 
    ```bash
    Switch(config)# line vty 0
    Switch(config-line)# password <password>
    Switch(config-line)# login
    Switch(config-line)# exit
    ```
    Secure VTY lines (multi line) 1 to 15
    ```bash
    Switch(config)# line vty 0
    Switch(config-line)# password <password>
    Switch(config-line)# login
    Switch(config-line)# exit
    ```
* Secure privileged EXEC mode
    ```bash
    Switch(config-line)# line vty 1 15
    Switch(config-line)# enable password <password>
    Switch# login
    Switch# exit
    ```
    Note : Enable password is a **legacy command**
* Encrypt all passwords
    ```bash
    Switch(config)# service password-encryption
    ```

[Back to Top](#cisco-cli-commands)

## IP Addressing Switch
* Show mac address table
    ```bash
    Switch# show mac-address-table
    ```
* Assign IP to VLAN 1 (default VLAN)
    ```bash
    Switch> enable
    Switch# config terminal
    Switch(config)# interface vlan1
    Switch(config-if)# ip address 192.168.1.2 255.255.255.0
    Switch(config-if)# no shutdown
    ```
* Configure Default Gateway
    ```bash
    Switch(config)# ip default-gateway 192.168.1.1
    ```

[Back to Top](#cisco-cli-commands)

## Switch Port
* Configure  port speed and duplex auto sensing. 
    ```bash
    Switch> enable
    Switch# config terminal
    Switch(config)# interface fa0/2
    Switch(config-if)# speed 10
    Switch(config-if)# duplex half
    Switch(config-if)# description Some text description here
    ```
* Switch port security via mac address. Allow mac address 0000.0000.0000 on port fa0/2 only. **Manually inputting mac address**.
    ```bash
    Switch(config)# interface fa0/2
    Switch(config-if)# switchport mode access
    Switch(config-if)# switchport port-security
    Switch(config-if)# switchport port-security mac-address 0000.0000.0000
    ```
    Turn off port security
    ```
    Switch(config-if)# no switchport port-security mac-address  0000.0000.0000
    ```
* Switch port security via mac address. Allow mac address 0000.0000.0000 on port fa0/2 only. **Automatically sensing the mac address** by learning only 1 address and shutdown if violation occurs.
    ```bash
    Switch(config)# interface fa0/2
    Switch(config-if)# switchport mode access
    Switch(config-if)# switchport port-security
    Switch(config-if)# switchport port-security mac-address sticky
    Switch(config-if)# switchport port-security maximum 1
    Switch(config-if)# switchport port-security violation shutdown
    ```
* Show port security
    ```bash
    Switch# show port-security address
    ```
* Display all security settings for interface fa0/2
    ```bash
    Switch# show port-security interface fa0/2
    ```

 [Back to Top](#cisco-cli-commands)

## VLANs
* Show current VLAN settings
    ```bash
    Switch# show vlan brief
    ```
* Create several VLAN and put a name description.
    ```bash
    Switch(config)# vlan 10
    Switch(config-vlan)# name Admin
    Switch(config-vlan)# exit
    Switch(config)# vlan 20
    Switch(config-vlan)# name Payroll
    Switch(config-vlan)# exit
    Switch(config)# vlan 30
    Switch(config-vlan)# name Research
    Switch(config-vlan)# exit
    Switch(config)# vlan 100
    Switch(config-vlan)# name Wireless
    Switch(config-vlan)# exit
    ```
* Assign ports to VLAN. Assign fastEthernet 0/3 to vlan 10
    ```bash
    Switch(config)# interface fastEthernet 0/3
    Switch(config-if)# switchport mode access 
    Switch(config-if)# switchport access vlan 10 
    Switch(config-if)# exit
    ```
* Remove a port from a vlan. Remove fastEthrnet 0/2 from vlan 50. Then delete vlan 50
    ```bash
    Switch(config)# interface fastEthernet 0/2
    Switch(config-if)# no switchport access vlan 50 
    Switch(config-if)# exit
    Switch(config)# no vlan 50 
    ```
* Assign a range of port to a vlan. Assign port 5 to 9 to vlan 30
    ```bash
    Switch(config)# interface range fastEthernet 0/5-9
    Switch(config-if-range)# switchport mode access 
    Switch(config-if-range)# switchport access vlan 30 
    Switch(config-if)# exit
    ```
* Create a trunk port
    ```bash
    Switch> enable
    Switch# config terminal
    Switch(config)# interface fa0/24
    Switch(config-if)# switchport mode trunk
    Switch(config-if)# exit
    ```
    Show trunk port
    ```bash
    Switch(config)# show interfaces trunk
    ```

 [Back to Top](#cisco-cli-commands)

## Router
* Show information about the Interfaces
    ```bash
    Router# show interfaces
    ```
* Show current configuration in RAM
    ```bash
    Router# show run
    ```   
* Summary of all enabled interfaces including name and status 
    ```bash
    Router# show ip interface brief
    ```
* Assign IP to router
    ```bash
    Router(config)# interface fastEthernet 0/0
    Router(config-if)# ip address 192.168.1.1 255.255.255.0
    Router(config-if)# no shutdown
    ```
* Serial interfaces IP configuration
    ```bash
    Router(config)# interface serial 0/0/0
    Router(config-if)# ip address 192.168.2.1 255.255.255.0
    Router(config-if)# clock rate 128000
    Router(config-if)# description WAN Connection
    Router(config-if)# no shutdown
    ```
    ```bash
    Router(config)# interface serial 0/0/1
    Router(config-if)# ip address 172.16.0.1 255.255.0.0 
    Router(config-if)# no shut
    Router(config-if)# encapsulation frame-relay
    ```
* Configure loop back address
    ```bash
    Router(config)# interface loopback 0
    Router(config-if)# ip address 192.168.255.1 255.255.255.0
    ```
* Assign IP to Ethernet interfaces
    ```bash
    Router(config)# interface fastEthernet 0/0
    Router(config-if)# ip address 192.168.1.1 255.255.255.0 
    Router(config-if)# no shut
    Router(config-if)# description This is the description
    ```
* Assign IP to Serial interfaces
    ```bash
    Router(config)# interface serial 0/0/0
    Router(config-if)# ip address 192.168.2.1 255.255.255.0 
    Router(config-if)# clock rate 128000 
    Router(config-if)# description This is the description
    Router(config-if)# no shut
    ```
    Note: *Clock rate* is the speed of the link

[Back to Top](#cisco-cli-commands)

## Routing
* Show routing table
    ```bash
    Router# show ip route
    ```
* Recursive static route:  Or next hop route 
  ```ip route <destination nework> <subnetmask> <next_hop_ip>``` 
    ```bash
    Router# ip route 192.168.5.0 255.255.255.0 192.168.2.2
    ```
* Directly connected (exit interface) static route 
    ```ip route <destination nework> <subnetmask> <outgoing interface>```
    ```bash
    Router# ip route 192.168.5.0 255.255.255.0 s0/0/0
    ```
* Default static route (last resort) usually going to ISP 
    ```ip route 0.0.0.0. 0.0.0.0 <outgoing interface>```
    ```bash
    Router(config)# ip route 0.0.0.0 0.0.0.0 s0/0/1
    ```

[Back to Top](#cisco-cli-commands)

## Dynamic Routing
* Enabling and configuring RIPv2
    ```bash
    Router(config)# router rip
    Router(config-router)# version 2
    Router(config-router)# network 192.168.1.0
    Router(config-router)# network 192.168.2.0
    Router(config-router)# network 192.168.255.0
    ```
* Stop RIP updates (to other devices)
    ```bash
    Router(config)# router rip
    Router(config-router)# passive-interface fastEthernet 0/0
    ```
* Advertise 0.0.0.0 to other router
    ```bash
    Router(config)# router rip
    Router(config-router)# default-information originate
    ```
[Back to Top](#cisco-cli-commands)

## IPv6 Commands
* Enable the router to forward IPv6 packets.
    ```bash
    Router(config)# ipv6 unicast-routing
    ```
* Configure IPv6 addressing on GigabitEthernet0/0.
    ```bash
    Router(config-if)# ipv6 address 2001:db8:1:1::1/64
    Router(config-if)# ipv6 address fe80::1 link-local
    Router(config-if)# no shutdown
    ```
* Show configuration
    ```bash
    Router# show ipv6 interface brief
    ```
* Remove address
    ```bash
    Router(config-if)# no ipv6 address 2001:db8:1:5::1/64
    ```

[Back to Top](#cisco-cli-commands)

## Basic Router Security
* Encrypt all plaintext passwords.
    ```bash
    Router(config)# service password-encryption
    ```
*  Set the minimum password length to 10.
    ```bash
    Router(config)# security password min-length 10
    ```
* Disable IP lookup
    ```bash
    Router(config)# no ip domain-lookup
    ```
* Set the domain name
    ```bash
    Router(config)# ip domain-name CCNA.com
    ```
* Create a user of your choosing with a strong encrypted password.
    ```bash
    Router(config)# username any_user secret any_password
    ```
* Modulus bits : Generate 1024-bit RSA keys
    ```bash
    Router(config)# crypto key generate rsa
    The name for the keys will be: RTA.CCNA.com
    Choose the size of the key modulus in the range of 360 to 2048 for your
    General Purpose Keys. Choosing a key modulus greater than 512 may take
    a few minutes.
    
    How many bits in the modulus [512]: 1024
    ```
* Block anyone for three minutes who fails to log in after four attempts within a two-minute period
    ```bash
    Router(config)# login block-for 180 attempts 4 within 120
    ```
* Configure all VTY lines for SSH access and use the local user profiles for authentication.
    ```bash
    Router(config)# line vty 0 4
    Router(config-line)# transport input ssh
    Router(config-line)# login local
    ```
* Set the EXEC mode timeout to 6 minutes on the VTY lines.
    ```bash
    Router(config-line)# exec-timeout 6
    ```
* Turn off all unused port
    ```bash
    Switch(config)# interface range F0/2-24, G0/2
    Switch(config-if-range)# shutdown
    ```

[Back to Top](#cisco-cli-commands)

## Sample Command Sequence

### Switch
```
enable
config t

hostname S2

interface vlan1
ip address 192.168.1.2 255.255.255.0
ip default-gateway 192.168.0.1	
no shutdown
no ip domain-lookup

line console 0
password Ciscoconpa55
exec-timeout 5
login
exit

line vty 0
exec-timeout 5
login local

enable secret Ciscoenpa55

service password-encryption
```

[Back to Top](#cisco-cli-commands)

### Router

```
enable
config t
hostname R1

no ip domain-lookup

enable secret Ciscoenpa55

line console 0
password Ciscoconpa55
exec-timeout 10
login
exit

service password-encryption

banner motd #Authorized access only!#

ctrl-z
show ip interface brief

interface g0/0
ip address 192.168.1.1 255.255.255.0
no shutdown

ipv6 unicast-routing
ipv6 address 2001:db8:1:1::1/64
ipv6 address fe80::1 link-local

ip domain-name CCNA-lab.com

crypto key generate rsa
1024

line vty 0 4
transport input ssh
exec-timeout 5
login local

username Admin1 privilege 15 secret Admin1pa55

login block-for 180 attempts 4 within 120

security password min-length 10
```

[Back to Top](#cisco-cli-commands)


### Case Study : CCNA Level 1

**Topology**<br/><img src="pics/topology1.png">

**Scenario** <br/>
In this Case Study, you will configure the devices in a small network. You must configure a router, switch, and PCs to support both IPv4 and IPv6 connectivity. You will configure security, including SSH, on the router. In addition, you will test and document the network using common CLI commands. 
  
Given an IP address and mask of (address / mask), **172.16.16.0 mask 255.255.254.0** design an IP addressing scheme that satisfies the following requirements. Network address/mask and the number of hosts for Subnets A and B will be provided below.

| Subnet      | Number of Hosts |
| ----------- | ----------- |
| Subnet A      | 100       |
| Subnet B      | 200       |

**Answer**: **Subnet A**:

| Specification                     | Student Input         | 
| -----------                       | -----------           |
| New IP mask (CIDR format)	        | ```/25```             |
| New IP mask (dotted decimal)      | ```255.255.255.128``` |
| Number of usable hosts            | ```126```             |
| Network Address (Network IP)      | ```172.16.17.0```     |
| First IP Host address(usable)     | ```172.16.17.1```     |
| Last IP Host address(usable)      | ```172.16.17.126```   |
| Broadcast Address (Broadcast IP)  | ```172.16.17.127```   |

**Answer**: **Subnet B**:

| Specification                     | Student Input         | 
| -----------                       | -----------           |
| New IP mask (CIDR format)	        | ```\24```             |
| New IP mask (dotted decimal)      | ```255.255.255.0```   |
| Number of usable hosts            | ```254```             |
| Network Address (Network IP)      | ```172.16.16.0```     |
| First IP Host address(usable)     | ```172.16.16.1```     |
| Last IP Host address(usable)      | ```172.16.16.254```   |
| Broadcast Address (Broadcast IP)  | ```172.16.16.255```   |

Host **computers** will use the **FIRST usable IP address in the subnet** while the network **router** will use the **LAST usable address in the subnet**. The **switch** will use the **SECOND from the last usable address in the subnet**.

Write down the IP address information for each device:

| Device    | IP Addess     | Subnet Mask       | Gateway       |
| -------   | ----------    | -----------       | --------      |
| PC-A      | ```172.16.17.1```     | ```255.255.255.128```   | ```172.16.17.126``` |
| R1-G0/0   |``` 172.16.17.126``` |``` 255.255.255.128```   | NA            |  
| R1-G0/1   | ```172.16.16.254 ```| ```255.255.255.0 ```    | NA            |
| S1        | ```172.16.16.253 ```  |``` 255.255.255.0```     | ```172.16.16.254``` |
| PC-B      | ```172.16.16.1```   | ```255.255.255.0```     | ```172.16.16.254 ```|


#### Host Side Configuration
**IPv4**

| Device    | IP Addess     | Subnet Mask       | Gateway       |
| -------   | ----------    | -----------       | --------      |
| PC-A      | ```172.16.17.1```     | ```255.255.255.128```   | ```172.16.17.126``` |
| PC-B      | ```172.16.16.1```   | ```255.255.255.0```     | ```172.16.16.254 ```|

**IPv6**

Given an IPv6 network address of **2001:DB8:BEEF::/64**, configure IPv6 addresses for the Gigabit interfaces on R1. Use **FE80::1** as the link-local address on both interfaces.

| Device  | Interface   |  IPv6                                  | Gateway       |
| ------- | ----------  |  -----------                           | -----------   |
| R1      | g0/0        |  ```2001:db8:beef:a::1/64  ```               |  |
| R1      | g0/1        |  ```2001:db8:beef:b::1/64 ```                |  |
| PC-A    |             |  ```2001:DB8:BEEF:A:240:BFF:FEB2:6B7D/64```  | ```fe80::1``` |
| PC-B    |             |  ```2001:DB8:BEEF:B:290:21FF:FE91:5D96/64``` | ```fe80::1``` |

#### Router Side Configuration 

| Command                       | Specification     | Task          | 
| -------                       | ----------        | ----------    |
| ```erase startup-config```    |                   | Erase the startup-config file on the Router.  |   
| ```reload```                  |                   | Reload the Router.                            |
| ```enable``` <br> ```config t``` <br> ```no ip domain-lookup ```|                 | Disable DNS lookup|
| ```hostname R1```| R1              | Router name (case sensitive)|
| ```ip domain-name casestudy.com``` | casestudy.com   | Domain name (case sensitive)|
| ```enable secret ciscoenpass``` | ciscoenpass | Encrypted privileged exec password|
| ```line console 0``` <br> ```password ciscoconpass``` <br> ```login``` <br> ```exit``` | ciscoconpass | Console access password|
| ```security password min-length 8``` | 8 characters| Set the minimum length for passwords|
| ```username admin secret adminpass``` | Username: admin <br> Password: adminpass | Create a user with an encrypted password in the local database |
| ```line vty 0 4``` <br>  ```login local``` | | Set login on VTY 0 to 4 lines to use local database |
| ```transport input all``` | | Set VTY lines to accept all connections.|
| ```service password-encryption``` | | Encrypt the clear text passwords|
| ```banner motd #Warning! Unauthorized Access is Prohibited.# ```| Warning! Unauthorized Access is Prohibited. | MOTD Banner (case sensitive)|
| ```interface g0/0``` <br> ```description to LAN A```<br>```ip address 172.16.17.126 255.255.255.128``` <br> ```no shut``` | Set the description to LAN A <br> Set the Layer 3 IPv4 address <br> Activate Interface | Interface G0/0|
| ```interface g0/1``` <br> ```description to LAN B```<br>```ip address 172.16.16.254 255.255.255.0``` <br> ```no shut```| Set the description to LAN B <br> Set the Layer 3 IPv4 address <br> Activate Interface | Interface G0/1|
| ```crypto key generate rsa``` <br> ```1024``` | 1024 bits modulus | Generate a RSA crypto key|
| ```interface g0/0``` <br> ```ipv6 address 2001:DB8:BEEF:A::1/64``` <br> ```ipv6 address fe80::1 link-local```| Configure G0/0 to use the first address in subnet A. 2001:DB8:BEEF:A::/64 | Assign the IPv6 Global Unicast Address <br> Assign the IPv6 link-local address |
| ```interface g0/1 ``` <br>```ipv6 address 2001:DB8:BEEF:B::/64``` <br> ```ipv6 address fe80::1 link-local``` | Configure G0/0 to use the first address in subnet B. 2001:DB8:BEEF:B::/64 |  Assign the IPv6 Global Unicast Address <br> Assign the IPv6 link-local address |
| ```ipv6 unicast-routing ```|  |Enable IPv6 unicast routing.|

#### Switch Side Configuration 

| Command                       | Specification     | Task          | 
| -------                       | ----------        | ----------    | 
| ```erase startup-config```    |                   | Erase the startup-config file on the Switch.   |   
| ```delete flash:vlan.dat```   |                   | Delete the vlan.dat file on the Switch   | 
| ```reload```                  |                   | Reload the Switch.                              |
| ```enable``` <br> ```config t``` <br> ```hostname S1```| S1              | Router name (case sensitive)|
| ```interface vlan1```<br>```ip address 172.16.16.253 255.255.255.0```<br>```no shutdown``` | Set the Layer 3 IPv4 address <br> Activate Interface | Configure Management Interface (SVI)|
| ```exit```<br> ```ip default-gateway 172.16.16.254```|               | Set the default gateway|
| ```enable secret ciscoenpass```| ciscoenpass              | Encrypted privileged exec password(case sensitive)|
| ```line console 0``` <br> ```password ciscoconpass``` <br> ```login``` <br> ```exit```| ciscoconpass              | Console access password(case sensitive)|
| ```line vty 0 15```<br>```transport input telnet```<br>```password ciscovtypass```<br>```login local```| ciscovtypass              | Telnet access password ( vty line 0 to 15) – allow only telnet(case sensitive)|

#### Other Commands
| Command                                   | Description       | 
| -------                                   | ----------        | 
| ```show ip interface brief```             | Display a summary of important information about the interfaces on R1.|
| ```show ip route```                       | Display the IPv4 routing table.|
| ```show arp```                            | Display the Layer 2 to Layer 3 mapping of addresses on R1.|
| ```show ip interface G0/0```              | Display detailed IPv4 information about interface G0/0 on R1.|
| ```show ipv6 route```                     | Display the IPv6 routing table.|
| ```show ipv6 interface brief```           | Display a summary of IPv6 interface addresses and status.|
| ```show cdp neighbors```                  | Display information about the devices connected to R1. Information should include Device ID, Local Interface, Hold time, Capability, Platform, and Port ID.|
| ```copy running-config startup-config```  | Save the current configuration so it will be used the next time the router is started.|

<br/><br/>

# CCNA II : Switching, Routing, and Wireless Essentials

| Command                       | Specification     | Task          | 
| -------                       | ----------        | ----------    | 
| ```sdm prefer dual-ipv4-and-ipv6 default ```    |                   |The switch may need to be configured for IPv6.   |   
| ```cmc```   | asd                 | asd | 

## Switch SVI Configuration Example
| Command                       | Specification     | Task          | 
| -------                       | ----------        | ----------    | 
|	```S1# configure terminal```	|	|	Enter global configuration mode.	|
|	```S1(config)# interface vlan 99```	|	|	Enter interface configuration mode for the SVI.	|
|	```S1(config-if)# ip address 172.17.99.11 255.255.255.0```	|	|	Configure the management interface IPv4 address.	|
|	```S1(config-if)# ipv6 address 2001:db8:acad:99::1/64```	|	|	Configure the management interface IPv6 address	|
|	```S1(config-if)# no shutdown```	|	|	Enable the management interface.	|
|	```S1(config-if)# end```	|	|	Return to the privileged EXEC mode.	|
|	```S1# copy running-config startup-config```	|	|	Save the running config to the startup config.	|

## VLAN Configuration
* Display current VLANs
    ```
    Switch# show vlan brief
    ```
* Create VLANs
    ```
    Switch(config)# vlan 10
    Switch(config-if)# name Faculty/Staff
    Switch(config-if)# vlan 20
    Switch(config-if)# name Students
    Switch(config-if)# vlan 30
    Switch(config-if)# name Guest(Default)
    Switch(config-if)# vlan 99
    Switch(config-if)# name Management&Native
    Switch(config-if)# vlan 150
    Switch(config-if)# name VOICE
    ```
* Assign an interface to VLAN
    ```
    Switch(config)# interface f0/11
    Switch(config-if)# switchport mode access
    Switch(config-if)# switchport access vlan 10
    ```
* Assign voice VLAN
    ```
    Switch(config)# interface f0/18
    Switch(config-if)# mls qos trust cos
    Switch(config-if)# switchport voice vlan 150
    ```
* Port Status
    ```
    Switch# show interfaces fa0/18 switchport
    ```

## Configure Trunks
* Configure G0/1 and G0/2 interfaces for tunking
    ```
    Switch(config)# interface range g0/1-2
    Switch(config-if)# switchport mode trunk
    ```
* Configure vlan 99 as the native vlan for G0/1 and G0/2 interfaces
    ```
    Switch(config)# interface range g0/1-2
    Switch(config-if)# switchport mode trunk
    Switch(config-if) switchport trunk native vlan 99
    ```

## Dynamic Trunking Protocol(DTP)
 * Disable DTP negotiation
    ```
    Switch(config)# interface range g0/1-2
    Switch(config-if)# switchport mode trunk
    Switch(config-if)# switchport nonegotiate
    ```
* Configure the trunk link to **Dynamic Desirable** on G0/1
    ```
    Switch(config)# interface g0/1
    Switch(config-if)# switchport mode dynamic desirable
    ```
* Verify status of DTP
    ```
    Switch(config)# show dtp
    ```
* verify trunking is enabled
    ```
    Switch(config)# show interfaces trunk
    ```

## 802.1Q Encapsulation
* Create AUbinterface G0/0.10
  * Set encapsulation type to 802.1Q and assign VLAN10 to the subinterface
    ```
    Router(config)# int g0/0.10
    Router(config-if)# encapsulation dot1Q 10
    Router(config-if)# ip address 172.17.10.1 255.255.255.0
    ```

## Activity : Configure Layer 3 Switching and Inter-VLAN Routing

* Objectives:
  * Part 1 : [Configure Layer 3 Switching](#part-1--configure-layer-3-switching)
  * Part 2 : [Configure Inter-VLAN Routing](#part-2--configure-inter-vlan-routing)
  * Part 3 : [Configure IPv6 Inter-VLAN Routing](#part-3--configure-ipv6-inter-vlan-routing)
<br><br>
* **Scenario** :  A multilayer switch like the Cisco Catalyst 3650 is capable of both Layer 2 switching and Layer 3 routing. One of the advantages of using a multilayer switch is this dual functionality. A benefit for a small to medium-sized company would be the ability to purchase a single multilayer switch instead of separate switching and routing network devices. Capabilities of a multilayer switch include the ability to route from one VLAN to another using multiple switched virtual interfaces (SVIs), as well as the ability to convert a Layer 2 switchport to a Layer 3 interface. <br><img src="pics/activity_table1.png" width="500"><br><img src="pics/activity_diagram.png" width="500">

### Part 1 : Configure Layer 3 Switching
* Configure the GigabitEthernet 0/2 port on switch MLS as a routed port and verify that you can ping another Layer 3 address.
  - On MLS, configure G0/2 as a routed port and assign an IP address according to the Addressing Table.
    ```bash
    MLS(config)# interface g0/2
    MLS(config-if)# no switchport
    MLS(config-if)# ip address 209.165.200.225 255.255.255.252
    ```
  - Verify connectivity to Cloud by pinging 209.165.200.226.
    ```bash
    MLS# ping 209.165.200.226

    Type escape sequence to abort.
    Sending 5, 100-byte ICMP Echos to 209.165.200.226, timeout is 2 seconds:
    !!!!!
    Success rate is 100 percent (5/5), round-trip min/avg/max = 0/0/0 ms
    ```

### Part 2 : Configure Inter-VLAN Routing
- **Step 1: Add VLANs** : Add VLANs to MLS according to the table below. Packet Tracer scoring is case-sensitive, so type the names exactly as shown.

    | VLAN Number   | VLAN Name     | 
    | -------       | ----------    |
    | 10            | Staff         |
    | 20            | Student       |
    | 30            | Faculty       |
    
    ```bash
    MLS(config)# vlan 10
    MLS(config)# name Staff
    MLS(config)# vlan 20
    MLS(config)# name Student
    MLS(config)# vlan 30
    MLS(config)# name Faculty
    ```
- **Step 2: Configure SVI on MLS** : Configure and activate the SVI interfaces for **VLANs 10, 20, 30, and 99** according to the Addressing Table. The configuration for VLAN 10 is shown below as an example.
    ```bash
    MLS(config)# interface vlan 10
    MLS(config-if)# ip address 192.168.10.254 255.255.255.0
    MLS(config-if)# ipv6 address 2001:db8:acad:10::1/64
    MLS(config)# interface vlan 20
    MLS(config-if)# ip address 192.168.20.254 255.255.255.0
    MLS(config-if)# ipv6 address 2001:db8:acad:20::1/64
    MLS(config)# interface vlan 30
    MLS(config-if)# ip address 192.168.30.254 255.255.255.0
    MLS(config-if)# ipv6 address 2001:db8:acad:30::1/64
    MLS(config)# interface vlan 99
    MLS(config-if)# ip address 192.168.99.254 255.255.255.0   
    ```
- **Step 3: Configure Trunking on MLS** : Trunk configuration differs slightly on a Layer 3 switch. On the Layer 3 switch, the trunking interface needs to be encapsulated with the dot1q protocol, however it is not necessary to specify VLAN numbers as it is when working with a router and subinterfaces.
  * On MLS, configure interface g0/1.
      ```bash
      MLS(config)# interface g0/1
      ```  
  * Make the interface a static trunk port.
      ```bash
      MLS(config-if)# switchport mode trunk
      ```
  * Specify the native VLAN as 99.
      ```bash
      MLS(config-if)# switchport trunk native vlan 99
      ```
  * Encapsulate the link with the dot1q protocol.
      ```bash
      MLS(config-if)# switchport trunk encapsulation dot1q
      ```
  Note: Packet Tracer may not score the trunk encapsulation.

- **Step 4: Configure Trunking on S1** :
  * Configure interface g0/1 of S1 as a static trunk.
    ```bash
    S1(config)# int g0/1
    S1(config-if)# switchport mode trunk
    ```
  * Configure the native VLAN on the trunk.
    ```bash
    S1(config-if)# switchport trunk native vlan 99
    ```

- **Step 5: Enable routing** :
  * Use the ```show ip route``` command. Are there any active routes?

  * Enter the ip routing command to enable routing in global configuration mode.
    ```bash
    MLS(config)# ip routing
    ```
  * Use the ```show ip route``` command to verify routing is enabled.
    ```bash
    MLS# show ip route
    Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
    D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
    N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
    E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
    i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
    * - candidate default, U - per-user static route, o - ODR
    P - periodic downloaded static route

    Gateway of last resort is not set

    C 192.168.10.0/24 is directly connected, Vlan10
    C 192.168.20.0/24 is directly connected, Vlan20
    C 192.168.30.0/24 is directly connected, Vlan30
    C 192.168.99.0/24 is directly connected, Vlan99
    209.165.200.0/30 is subnetted, 1 subnets
    C 209.165.200.224 is directly connected, GigabitEthernet0/2
    ```
- **Step 6: Verify end-to-end connectivity** :
  * From PC0, ping PC3 or MLS to verify connectivity within VLAN 10.
  * From PC1, ping PC4 or MLS to verify connectivity within VLAN 20.
  * From PC2, ping PC5 or MLS to verify connectivity within VLAN 30.
  * From S1, ping S2, S3, or MLS to verify connectivity with VLAN 99.
  * To verify inter-VLAN routing, ping devices outside the sender’s VLAN.
  * From any device, ping this address inside Cloud, 209.165.200.226.
  The Layer 3 switch is now routing between VLANs and providing routed connectivity to the cloud.

### Part 3 : Configure IPv6 Inter-VLAN Routing
Layer 3 switches also route between IPv6 networks.
- **Step 1: Enable IPv6 routing** : Enter the ipv6 unicast-routing command to enable IPv6 routing in global configuration mode.
  ```bash
  MLS(config)# ipv6 unicast-routing
  ```
- **Step 2: Configure SVI for IPv6 on MLS** : Configure IPv6 addressing on SVI for VLANs 10, 20, and 30 according to the Addressing Table. The configuration for VLAN 10 is shown below.
    ```bash
    MLS(config)# interface vlan 10
    MLS(config-if)# ipv6 address 2001:db8:acad:10::1/64
    ```
- **Step 3: Configure G0/2 with IPv6 on MLS**
  * Configure IPv6 addressing on G0/2.
    ```bash
    MLS(config)# interface G0/2
    MLS(config-if)# ipv6 address 2001:db8:acad:a::1/64
    ```
  * Use the show ipv6 route command to verify IPv6 connected networks.
    ```bash
    MLS# show ipv6 route
    IPv6 Routing Table - 10 entries
    Codes: C - Connected, L - Local, S - Static, R - RIP, B - BGP
    U - Per-user Static route, M - MIPv6
    I1 - ISIS L1, I2 - ISIS L2, IA - ISIS interarea, IS - ISIS summary
    O - OSPF intra, OI - OSPF inter, OE1 - OSPF ext 1, OE2 - OSPF ext 2
    ON1 - OSPF NSSA ext 1, ON2 - OSPF NSSA ext 2
    D - EIGRP, EX - EIGRP external
    S ::/0 [1/0]
    via 2001:DB8:ACAD:A::2, GigabitEthernet0/2
    C 2001:DB8:ACAD:A::/64 [0/0]
    via ::, GigabitEthernet0/2
    L 2001:DB8:ACAD:A::1/128 [0/0]
    via ::, GigabitEthernet0/2
    C 2001:DB8:ACAD:10::/64 [0/0]
    via ::, Vlan10
    L 2001:DB8:ACAD:10::1/128 [0/0]
    via ::, Vlan10
    C 2001:DB8:ACAD:20::/64 [0/0]
    via ::, Vlan20
    L 2001:DB8:ACAD:20::1/128 [0/0]
    via ::, Vlan20
    C 2001:DB8:ACAD:30::/64 [0/0]
    via ::, Vlan30
    L 2001:DB8:ACAD:30::1/128 [0/0]
    via ::, Vlan30
    L FF00::/8 [0/0]
    via ::, Null0
    ```

- **Step 4: Verify IPv6 connectivity** : Devices PC3, PC4, and PC5 have been configured with IPv6 addresses. Verify IPv6 inter-VLAN routing and connectivity to Cloud.
  * From PC3, ping MLS to verify connectivity within VLAN 10.
  * From PC4, ping MLS to verify connectivity within VLAN 20.
  * From PC5, ping MLS to verify connectivity within VLAN 30.
  * To verify inter-VLAN routing, ping between devices PC3, PC4, and PC5.
  * From PC3 ping the address inside Cloud, 2001:db8:acad:a::2.

[Back to Top](#cisco-cli-commands)