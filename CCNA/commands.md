# Cisco CLI Commands

<!-- TOC -->

- [Cisco CLI Commands](#cisco-cli-commands)
  - [Sample Sequence](#sample-sequence)

<!-- /TOC -->


## Sample Sequence
* ### Switch
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


* ### Router

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


