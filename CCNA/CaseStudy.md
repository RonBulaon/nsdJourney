# Case Study

R1:
```bash
Router>
Router>enable
Router#erase startup-config 
Router#reload

Router>enable
Router#configure terminal 
Router(config)#no ip domain lookup 
Router(config)#hostname R1
R1(config)#ip domain name ccna-lab.com

```

S1 and S2
```bash
Switch>enable
Switch#erase startup-config 
Switch#reload

Switch>enable 
Switch#configure terminal 
Switch(config)#no ip domain lookup 

Switch(config)#sdm prefer dual-ipv4-and-ipv6 default
Switch#reload
```

