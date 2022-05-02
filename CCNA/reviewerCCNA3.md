# Reviewer

<!-- TOC -->

- [Reviewer](#reviewer)
  - [Basic Device Settings](#basic-device-settings)
  - [Site-to-Site GRE VPN](#site-to-site-gre-vpn)
  - [Single Area OSPFv2 (Router1/RouteRouter2)](#single-area-ospfv2-router1routerouter2)
    - [Other Settings](#other-settings)
  - [Site-to-Site IPsec VPN](#site-to-site-ipsec-vpn)
  - [NAT(Static, Dynamic, PAT)](#natstatic-dynamic-pat)
  - [ACL(Standard, Extended)](#aclstandard-extended)
  - [NTP and clock](#ntp-and-clock)
  - [CDP](#cdp)
  - [Test Connectivity](#test-connectivity)
  - [Backup](#backup)
  - [Restore](#restore)

<!-- /TOC -->

## Basic Device Settings
 * Reset switch/router to factory default. delete startup-config and vlan.dat
    ```bash
    Switch# erase startup-config 
    Switch# delete flash:vlan.dat
    Switch# show flash
    Switch# show start
    Switch# reload
    ```
* Disable DNS lookup
    ```bash
    Switch(config) #no ip domain-lookup
    ```
* Router/Switch name
    ```bash
    Switch(config)# hostname S1
    ```
* Domain name
    ```bash
    Router(config)# ip domain-name CCNA.com
    ```
* Encrypted privileged EXEC password
    ```bash
    Router(config)# enable secret ciscoenpass
    ```
* Console access password
    ```bash
    Router(config)# line console 0
    Router(config)# password ciscoconpass
    Router(config)# login
    Router(config)# exit
    ```
* Shutdown all unused interfaces
    ```bash
    SW-1# show ip interface brief 
    SW-1(config)# int range f0/3-9, f0/11-23
    SW-1(config-if-range)# shut
    SW-1(config-if-range)# exit
    ```
* Create an administrative user in the local database
    ```bash
    S1(config)#username admin secret admin1pass
    ```
* Set login on VTY lines to use local database and to accept SSH connections only
    ```bash
    S1(config)#line vty 0 15
    S1(config-line)#login local 
    S1(config-line)#transport input ssh 
    S1(config-line)#exit
    ```
* Encrypt the clear text passwords
    ```bash
    S1(config)#service password-encryption 
    ```
* Configure an MOTD Banner
    ```bash
    S1(config)#banner motd #Authorized access only#
    ```
* Generate an RSA crypto key
    ```bash
    S1(config)#crypto key generate rsa 
    How many bits in the modulus [512]: 1024
    ```
* Configure Management Interface (SVI) for VLAN 1 (the Management VLAN)
    ```bash
    S1(config)# interface vlan 1
    S1(config-if)#ip address 192.168.1.2 255.255.255.0
    S1(config-if)#no shutdown 
    S1(config-if)#exit
    ```
* Configure Default Gateway
    ```bash
    S1(config)#ip default-gateway 192.168.1.1
    ```
* Set the minimum length for passwords
    ```bash
    Router(config)#security passwords min-length 10
    ```
* Configure interface G0/0/1 and G0/0/1
    ```bash
    Router(config)#interface g0/0/0
    Router(config-if)#description Connect to network
    Router(config-if)#ip address 192.168.1.1 255.255.255.0
    Router(config-if)#no shutdown 

    Router(config-if)#interface g0/0/1
    Router(config-if)#description Connect to network
    Router(config-if)#ip address 192.168.1.1 255.255.255.0
    Router(config-if)#no shutdown
    ```
* Configure interface Lo0
    ```bash
    Router1(config-if)##interface loopback 0
    Router1(config-if)#ip address 192.168.1.1 255.255.255.0
    Router1(config-if)#exit
    ```

## Site-to-Site GRE VPN
* [Check this out](assignments.md/#configuring-gre)

## Single Area OSPFv2 (Router1/RouteRouter2)
* Configure the OSPF routing process. Use process id 1
    ```bash
    Router1(config)#router ospf 1
    ```
    ```bash
    RouteRouter2(config)#router ospf 1
    ```
* (optional) Manually configure the router id. Use 0.0.0.1 for Router1 and 0.0.0.2 for RouteRouter2
    ```bash
    Router1(config-router)#router-id 0.0.0.1
    ```
    ```bash
    RouteRouter2(config-router)#router-id 0.0.0.2
    ```
* Configure network statements. Configure a network statement for each locally attached network using a wild card mask that matches each network’s subnet mask Note: RouteRouter2 Lo0 network should not be included in the OSPF process.
    ```bash
    Router1(config-router)#network 10.67.254.0 0.0.0.3 area 0
    Router1(config-router)#network 192.168.1.0 0.0.0.255 area 0
    Router1(config-router)#network 10.52.0.0 0.0.0.7 area 0
    ```
    ```bash
    Router2(config-router)#network 10.67.254.0 0.0.0.3 area 0
    Router2(config-router)#network 10.67.1.0 0.0.0.255 area 0
    ```
### Other Settings
* Configure passive interfaces.Configure all interfaces that are not directly connected to an OSPF neighbor to be passive.
    ```bash
    Router1(config)#router ospf 1
    Router1(config-router)#passive-interface g0/0/1
    Router1(config-router)#passive-interface loopback 0
    Router1(config-router)#exit
    ```
* Configure the reference bandwidth. Adjust the reference bandwidth to 1 Gigabit.
    ```bash
    Router1(config)#router ospf 1
    Router1(config-router)#auto-cost reference-bandwidth 1000
    Router1(config-router)#exit
    ```
* Configure Loopback 0 to report the mask it is configured with instead of a host mask. Configure Loopback0 as a point-to-point network for OSPF.
    ```bash
    Router1(config)#interface loopback 0
    Router1(config-if)#ip ospf network point-to-point 
    Router1(config-if)#exit
    ```
* Tune the timers for your network	Configure the hello time for 30 seconds
    ```bash
    Router1(config)#interface g0/0/0
    Router1(config-if)#ip ospf hello-interval 30
    ```
* Provide default routing for the OSPF domain. Configure a static default route with loopback 0 as the exit interface, then share the default information with other OSPF speakers.
    ```bash
    Router2(config)#ip route 0.0.0.0 0.0.0.0 loopback 0
    Router2(config)#router ospf 1
    Router2(config-router)#default-information originate 
    Router2(config-router)#exit 
    ```

* Tune the DR/BDR election to favor R2. Set the OSPF priority for R2 to a value of 50.
    ```bash
    Router2(config)#interface g0/0/0
    Router2(config-if)#ip ospf priority 50
    Router2(config-if)#exit
    ```
## Site-to-Site IPsec VPN
  * [Check out this](assignments.md/#1024-configure-and-veridy-ntp)

## NAT(Static, Dynamic, PAT)
Remove 192.168.1.0/24 from OSPF	Remove the appropriate network statement at R1	2 points
Create an ACL to identify hosts allowed to be translated	Create an ACL that matches the 192.168.1.0 network	2 points
Configure Port Address Translation on the outside interface of R1	Configure the NAT association between the ACL and the interface g0/0/0 so that it uses port address translation	2 points
Identify the interfaces involved in NAT	Specify inside or outside on the appropriate interfaces	2 points


## ACL(Standard, Extended)
* Create an access control list	R2-SECURITY	
    ```bash
    R2(config)#ip access-list extended R2-SECURITY
    ```
* Control HTTP and HTTPS traffic.Only hosts from the 10.0.0.0/8 network are allowed to reach the web server at 209.165.201.1. *Note*: Considering that ```10.0.0.0/8``` is at g0/0/0
    ```bash
    R2(config-ext-nacl)#deny tcp any host 209.165.201.1 eq 443
    ```
* Control SSH traffic, SSH is not allowed to the address 209.165.201.1
    ```bash
    R2(config-ext-nacl)#deny tcp any host 209.165.201.1 eq 22
    ```
* Permit traffic. All other traffic, regardless of protocol, is allowed.
    ```bash
    R2(config-ext-nacl)#permit ip any any 
    ```
* Apply the ACL	Filter traffic originating from R1
    ```bash
    R2(config)#interface g0/0/0
    R2(config-if)#ip access-group R2-SECURITY in
    ```

## NTP and clock
* Configure HQ to use the device at 192.168.1.254 as an NTP server.
    ```bash
    HQ(config)#ntp server 192.168.1.254
    ```
* Set date and time
    ```bash
    R1# clock set 16:01:00 sept 25 2020 
    ```

## CDP
* Verify
    ```bash
    Router# show cdp
    Router# show cdp neighbors
    Router# show cdp interface
    ```
* Enable globally
    ```
    Router(config)# no cdp run
    Router(config)# exit
    Router# show cdp
    CDP is not enabled
    Router# configure terminal
    Router(config)# cdp run
    ```
* Activate CDP on the Branch router.
    ```bash
    Branch(config)#cdp run
    ```
* Enable/Disable in individual interface
    ```bash
    Switch(config)# interface gigabitethernet 0/0/1
    Switch(config-if)# cdp enable
    Switch(config-if)# no cdp enable
    ```

## Test Connectivity
* Ping 

## Backup 
* Copy the running configuration to flash memory.
    ```bash
    R1# copy running-config flash:
    Destination filename [running-config]? R1-running-config-backup
    ```

* Localfile to TFTP server
    ```bash
    Router#copy running-config tftp
    Address or name of remote host []? 192.168.1.1
    ```
## Restore
* Copy the saved running-config file from flash to update the running-config.
    ```bash
    Router# copy flash: running-config
    Source filename []? R1-running-config-backup
    ```