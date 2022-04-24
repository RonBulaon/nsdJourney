#!/usr/bin/env python3
import sys,ipaddress

if __name__=="__main__":
    ipi = ipaddress.ip_interface(sys.argv[1])
    print("Address \t", ipi.ip)
    print("Mask \t\t", ipi.netmask)
    print("Cidr \t\t", str(ipi.network).split('/')[1])
    print("Network \t", str(ipi.network).split('/')[0])
    print("Broadcast \t", ipi.network.broadcast_address)