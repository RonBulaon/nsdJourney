Router
```bash
MLS(config)# interface g0/2
MLS(config-if)# no switchport
MLS(config-if)# ip address 209.165.200.225 255.255.255.252

MLS(config)# vlan 10
MLS(config)# name Staff
MLS(config)# vlan 20
MLS(config)# name Student
MLS(config)# vlan 30
MLS(config)# name Faculty

MLS(config)# interface vlan 10
MLS(config-if)# ip address 192.168.10.254 255.255.255.0

MLS(config)# interface vlan 20
MLS(config-if)# ip address 192.168.20.254 255.255.255.0

MLS(config)# interface vlan 30
MLS(config-if)# ip address 192.168.30.254 255.255.255.0

MLS(config)# interface vlan 99
MLS(config-if)# ip address 192.168.99.254 255.255.255.0 

MLS(config)# interface g0/1
MLS(config-if)# switchport mode trunk
MLS(config-if)# switchport trunk native vlan 99
MLS(config-if)# switchport trunk encapsulation dot1q

MLS(config)# ip routing
MLS(config)# ipv6 unicast-routing

MLS(config)# interface vlan 10
MLS(config-if)# ipv6 address 2001:db8:acad:10::1/64

MLS(config)# interface vlan 20
MLS(config-if)# ipv6 address 2001:db8:acad:20::1/64

MLS(config)# interface vlan 30
MLS(config-if)# ipv6 address 2001:db8:acad:30::1/64

MLS(config)# interface G0/2
MLS(config-if)# ipv6 address 2001:db8:acad:a::1/64
```

Switch
```bash
S1(config)# int g0/1
S1(config-if)# switchport mode trunk
S1(config-if)# switchport trunk native vlan 99
```