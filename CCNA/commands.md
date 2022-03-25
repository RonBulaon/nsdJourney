# Table of Contents

<!-- TOC -->

- [Table of Contents](#table-of-contents)
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
- [CCNA II : Switching, Routing, and Wireless Essentials](#ccna-ii--switching-routing-and-wireless-essentials)
  - [Switch SVI Configuration Example](#switch-svi-configuration-example)
  - [VLAN Configuration](#vlan-configuration)
  - [Configure Trunks](#configure-trunks)
  - [Dynamic Trunking Protocol(DTP)](#dynamic-trunking-protocoldtp)
  - [802.1Q Encapsulation](#8021q-encapsulation)
  - [Spanning Tree Protocol (STP)](#spanning-tree-protocol-stp)
  - [EtherChannel](#etherchannel)

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
 [Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

 [Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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
[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)

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

[Back to Top](#table-of-contents)




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
    ```bash
    Switch# show vlan brief
    ```
* Create VLANs
    ```bash
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
    ```bash
    Switch(config)# interface f0/11
    Switch(config-if)# switchport mode access
    Switch(config-if)# switchport access vlan 10
    ```
* Assign voice VLAN
    ```bash
    Switch(config)# interface f0/18
    Switch(config-if)# mls qos trust cos
    Switch(config-if)# switchport voice vlan 150
    ```
* Port Status
    ```bash
    Switch# show interfaces fa0/18 switchport
    ```

## Configure Trunks
* Configure G0/1 and G0/2 interfaces for tunking
    ```bash
    Switch(config)# interface range g0/1-2
    Switch(config-if)# switchport mode trunk
    ```
* Configure vlan 99 as the native vlan for G0/1 and G0/2 interfaces
    ```bash
    Switch(config)# interface range g0/1-2
    Switch(config-if)# switchport mode trunk
    Switch(config-if)# switchport trunk native vlan 99
    ```

## Dynamic Trunking Protocol(DTP)
 * Disable DTP negotiation
    ```bash
    Switch(config)# interface range g0/1-2
    Switch(config-if)# switchport mode trunk
    Switch(config-if)# switchport nonegotiate
    ```
* Configure the trunk link to **Dynamic Desirable** on G0/1
    ```bash
    Switch(config)# interface g0/1
    Switch(config-if)# switchport mode dynamic desirable
    ```
* Verify status of DTP
    ```bash
    Switch(config)# show dtp
    ```
* verify trunking is enabled
    ```bash
    Switch(config)# show interfaces trunk
    ```

[Back to Top](#table-of-contents)

## 802.1Q Encapsulation
* Create AUbinterface G0/0.10
  * Set encapsulation type to 802.1Q and assign VLAN10 to the subinterface
    ```bash
    Router(config)# int g0/0.10
    Router(config-if)# encapsulation dot1Q 10
    Router(config-if)# ip address 172.17.10.1 255.255.255.0
    ```

## Spanning Tree Protocol (STP)
```bash
Switch(config)# show spanning-tree vlan 1
```

## EtherChannel
* Switch1 and SWitch2
  ```bash
  Switch1(config)# interface range f0/1-2
  Switch1(config)# channel-group 1 mode active
  ```
  ```bash
  Switch2(config)# interface range f0/1-2
  Switch2(config)# channel-group 1 mode active
  ```
* Check
  ```bash
  Switch2(config)# show ip interface
  Switch2(config)# show spanning-tree vlan 1
  Switch2(config)# show etherchannel summary
  ```

[Back to Top](#table-of-contents)

```
switchport trunk encapsulation dot1q
switchport no negotiate
```

