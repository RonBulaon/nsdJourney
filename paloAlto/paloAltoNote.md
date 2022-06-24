<h1>Palo Alto networks</h1>

<!-- TOC -->

- [Notes](#notes)
- [Lab 1 : Initial Configuration](#lab-1--initial-configuration)
- [Lab 2 : Interface Configuration](#lab-2--interface-configuration)
- [Lab 3 : Security and NAT Policies](#lab-3--security-and-nat-policies)
- [Configuration Flow](#configuration-flow)
- [Reset to Factory Default](#reset-to-factory-default)
- [CLI](#cli)
  - [Network Settings](#network-settings)
  - [Testing](#testing)
- [Settings/Configuration](#settingsconfiguration)
  - [MISC](#misc)
  - [Intial Configuation](#intial-configuation)
    - [Add an Admin Role Profile](#add-an-admin-role-profile)
    - [Add an Administrator Account](#add-an-administrator-account)
  - [Interface configuration](#interface-configuration)
    - [Create New Security Zones](#create-new-security-zones)
    - [Create Interface Management Profiles](#create-interface-management-profiles)
    - [Configure Ethernet Interfaces](#configure-ethernet-interfaces)
    - [Create a Virtual Wire](#create-a-virtual-wire)
    - [Create a Virtual Router](#create-a-virtual-router)
  - [Security and NAT Policies](#security-and-nat-policies)
    - [Create Tags](#create-tags)
    - [Create a Source NAT Policy](#create-a-source-nat-policy)
    - [Create Security Policy Rules](#create-security-policy-rules)
    - [Destination NAT : Create FTP Service from DMZ Server to Outside](#destination-nat--create-ftp-service-from-dmz-server-to-outside)
  - [App-ID](#app-id)
    - [Create an App-ID Security Policy Rule](#create-an-app-id-security-policy-rule)
    - [Enable Interzone Logging](#enable-interzone-logging)
    - [Enable the Application Block Page](#enable-the-application-block-page)
    - [Create an FTP Port-Based Security Policy Rule](#create-an-ftp-port-based-security-policy-rule)
    - [Migrate Port-Based Rule to Application-Aware Rule](#migrate-port-based-rule-to-application-aware-rule)
  - [Content-ID](#content-id)
  - [GlobalProtect](#globalprotect)
  - [Site to site VPN](#site-to-site-vpn)
  - [Active/Passive High Availability](#activepassive-high-availability)

<!-- /TOC -->

# Notes
* Cert Aligned to PCNSA
* Zone Based Firewall
  * Create a zone then attach interface with that zone
  * Stop attack at any point of Cyber-attack lifecycle
    * Reconnaisance
    * Weaponization
    * Delivery
    * Exploitation
    * Installation
    * Command and COntrol
    * Act on Objective
  * Panorama - will manage all firewall in single interface\
    * manageent andd reporting
  * Aperture - SAAS ; DLP alike
  * GlobalProtect - for endpoints; with agents.
  * AutoFocus
  * MineMeld
* Palo Alto networks Single Pass

# Lab 1 : Initial Configuration
* [Lab file](PAN9_EDU210_Lab_1.pdf)
  * 1.0 Connect to Your Student Firewall (page 6)
  * 1.1 Apply a Baseline Configuration to the Firewall (page 7)
  * 1.2 Add an Admin Role Profile (page 9)
  * 1.3 Add an Administrator Account (page 11)
  * 1.4 Test the policy-admin User (page 12)
  * 1.5 Take a Commit Lock and Test the Lock (page 14)
  * 1.6 Verify the Update and DNS Servers (page 17)
  * 1.7 Schedule Dynamic Updates (page 19)

# Lab 2 : Interface Configuration
* [Lab file](PAN9_EDU210_Lab_2.pdf)
  * 2.0 Load Lab Configuration (page 6)
  * 2.1 Create New Security Zones (page 9)
  * 2.2 Create Interface Management Profiles (page 10)
  * 2.3 Configure Ethernet Interfaces (page 12)
  * 2.4 Create a Virtual Wire (page 23)
  * 2.5 Create a Virtual Router (page 24)
  * 2.6 Test Connectivity (page 26)
  * 2.7 Modify Outside Interface Configuration (page 29)

# Lab 3 : Security and NAT Policies
* [Lab file](PAN9_EDU210_Lab_3.pdf)
  * 3.0 Load Lab Configuration (page 6)
  * 3.1 Create Tags (page 9)
  * 3.2 Create a Source NAT Policy (page 12)
  * 3.3 Create Security Policy Rules (page 14)
  * 3.4 Verify Internet Connectivity (page 18)
  * 3.5 Create FTP Service (page 19)
  * 3.6 Create a Destination NAT Policy (page 20)
  * 3.7 Create a Security Policy Rule (page 22)
  * 3.8 Test the Connection (page 26)



# Configuration Flow
# Reset to Factory Default
1. Connect the Console cable, which is provided by Palo Alto Networks, from the "**Console**" port to a computer, and use a terminal program (9600,8,n,1) to connect to the Palo Alto Networks device.

    *NOTE*: A USB-to-serial port will have to be used if the computer does not have a 9-pin serial port.

2. Enter your login credentials.

3. Enter the following CLI command:
    ```
    debug system maintenance-mode
    ```
    The firewall will reboot in the maintenance mode. 

4. When the firewall reboots, press Enter to continue to the **maintenance mode** menu.
Select **Factory Reset** and press **Enter**.

5. Select **Factory Reset** and press Enter again.

The firewall will reboot without any configuration settings. The default username and password to log in to the firewall is admin/admin.

# CLI
```
show system info                # IP address, uptime, and other config
show interface management       # 
```
Default credentials - 
admin/admin

```
configure  (sends to config mode)
set deviceconfig system ip-address 172.16.255.200 
set deviceconfig system  netmask 255.255.255.0
set deviceconfig system default-gateway 172.16.255.1
set deviceconfig system dns-setting servers primary 8.8.8.8
commit  
exit
```

## Network Settings


## Testing
```
ping host 8.8.8.
ping host www.paloaltonetworks.com
```
# Settings/Configuration
## MISC
* IP Address : Device > Setup > Interfaces > Management
* DNS : Device > Setup > Services, Click edit > Services Tab > add a DNS server.
* NTP : Device > Setup > Services, Click edit > NTP Tab > add IP of NTP server.
* Updates : Device > Dynamic Updates

## Intial Configuation
### Add an Admin Role Profile 
  * Device > Admin Role (blade) > [+]Add (pane)
  * Options : You can set permission according to access with the **Web UI** || **XML/REST API** || **Command Line**
 
### Add an Administrator Account
  * Device > Administrators (blade) > [+]Add (pane)
  * Options :
    * Name : Used for login 
    * Password
    * Administrator type
    * Administrator : Dynamic || Role based (choose any from **Admin Role Profile**)

## Interface configuration
* Ideal situation : One interface is to One Zone

### Create New Security Zones 
  * Network > Zones (blade) > [+]Add (pane)
  * Options : Relevant Name and Type

### Create Interface Management Profiles 
  * Network > Network Profiles (blade) > Interface Mgmt > [+]Add (pane)
  * Description : Allow dis-allow management services like ping, ssh, etc 
  * Map this Management profuile to Network > Interfaces > <Interface> > Advanced > Management Profile

### Configure Ethernet Interfaces  
  * Network > Interfaces (blade) > Ethernet (pane tab) > choose an interface
  * Options : Config Tab : Choose Zone or Create New
  * Options : IPv4 Tab : config IP static or dynamic
  * Options : Advanced : Other Info (tab) > Management Profile > CHoose Management Profile

### Create a Virtual Wire 
  * Network > Virtual Wires (blade) > [+]Add (pane)
  * Note : On interface configuration interface type should be virtual wire for both interfaces involved

### Create a Virtual Router  
  * Network > Virtual Routes > [+]Add (pane)
  * Options : Name the virtual Router then under Router Settings tab [+] Add all interfaces to be routed.
  * Test :
    ```
    admin@firewall-a> show interface ethernet1/1
    admin@firewall-a> show routing route
    admin@firewall-a> ping source 203.0.113.21 host 8.8.8.8 
    ```
  * Static Route Tab : add static route for outgoing (to internet)
  

## Security and NAT Policies
### Create Tags
  * Objects > Tag > [+]Add (pane)

### Create a Source NAT Policy
  * Policies > NAT > [+]Add (pane)
  * Options : Original Packet : Source -> zoneInside
  * Option : Translated Packet :  Translation Type -> Dynamic IP and POrt, use Interface address on Type. Interface probably the Exit interface IP.

### Create Security Policy Rules
  * Policies > Security > [+]Add (pane)
  * Must Check Tab : Source / Destination / ACtions (including profile)

### Destination NAT : Create FTP Service from DMZ Server to Outside
  * Objects > Services > Put in details for the service
  * Policies > NAT > [+]Add (pane)
    * Options : Original Packet Tab (SAMPLE)
      * Source Zone Click Add and select inside
      * Destination Zone inside
      * Destination Interface ethernet1/2
      * Service service-ftp
      * Destination Address Click Add and manually enter 192.168.1.1 (interface to be NATed to Service, entry point of the zone to FW)
    * Options : Transslated Packet Tab (SAMPLE)
      * Destination Address Translation Type Static IP
      * Translated Address 192.168.50.10 (address of DMZ Server or where the service is hosted)
  * Policies > Security > [+]Add (pane)
    * Options : Source Tab : Indicate source Zone and use any for Source address
    * Options : Destination Tab : Indicate destination Zone and address use the entry interface becauase this is the IP you want to server the NATed service.
    * Options : Service/URL Tab : Indicate the service created for this entry
    * ACtions : Action Tab : make sure its allow and schedule set accordingly AND enable Log at Session END

## App-ID
### Create an App-ID Security Policy Rule
  * Policies > Security > [Policy] > Application(tab) > Applications(pane) > [+]Add
  * THen choose the applications

### Enable Interzone Logging 
  * Policies > Security > Interzone-default > Actions (tab) > Log at Session Start (Put check)
  * Policies > Security > Interzone-default > Actions (tab) > Log at Session End (Put check)
  * Note : Edit is blocked by default, override it first

### Enable the Application Block Page 
  * Device > Response Pages > Application Block Page > Disabled(click) > Enable Application Block Page (put check)

### Create an FTP Port-Based Security Policy Rule
  * Policies > Security > [Policy] > Application(tab) > Applications(pane) > Any (select this)
  * Policies > Security > [Policy] > Application(tab) > Service/URL Category(pane) > Service > [+]Add (Service Name)
    * Service Name : Objects > Services > Put in details for the service

### Migrate Port-Based Rule to Application-Aware Rule
  * Policies > Security > [Policy] >  Destination > Destination Zone > [+]Add (Add your zone) 
  * Policies > Security > [Policy] >  Destination > Destination Address > Any (select this)
  * Policies > Security > [Policy] >  Application > [+]Add (Add your application) 
  * Policies > Security > [Policy] > Application(tab) > Service/URL Category(pane) > Service > [Drop-Down] application-default


## Content-ID
--Lab 5

## GlobalProtect
  * Summary : 
    1. Pick the FW acting as portal
    2. Create a certificate (signed by the CA)
    3. Create an authentication Profile
    4. Create SSL/TLS service profile
    5. Portal Settings
       1. General : Set Name, Interface and IP
       2. Authentication : Select SSL/TLS service profile (created Step 4)
          Client Authentication (Created step 3)
    6. Configure the gateway
   
  * Detailed 
  1. Configure a Subinterface 
      * Network > Interfaces > Ethernet > [interface] > advance > Untagged Subinterface (checked)
      * [+] Add Subinterface (lower menu)

  2. Generate Self-Signed Certificates
      * Device > Certificate Management > Certificates > Generate (lower Menu)
  
  3.  Configure the SSL-TLS Service Profile 
      *  Device > Certificate Management > SSL/TLS > [+]Add
      *  One for each portal
   
  4.  Configure the LDAP Server Profile
      * Device > Server PRofiles > LDAP
        * Create or add new
  
  5.  Configure the Authentication Profile 
      * Device Authentication Profile > [+]Add (lower menu)
        * Authentication Tab : Type, server profile (from ldap profile), User Domain
        * Advance : give access to all or specific user
  
  6.  Configure the Tunnel Interface
      * Network > Interfaces > Tunnel > [+] Tunnel
  
  7.  Configure the Internal/External Gateway 
      * Network > GLobalProtect > GAteways > [+] Add
        * General : Name, interface (internal/external facing), IPv4
        * Authentication : SSL/TLS Profile (created above)
        * [+] Add 
          * Name, OS (Any), Authentication Profile (from above)

  8.  Configure the Portal
      * Network > GlobalProtect > Portals > [+] Add
        * General : name, interface, ipv4 
        * Authentication : SSL/TLS Profile (created above) > [+] Add
          * Name, OS, Authentication Profile
        * Agent : Trusted CA > [+]Add > locate CA from above steps
        * Agent : Agent > [+]Add
          * Authentication : Name
          * Internal : internal Host direction (checked), Ip address, hostname > [+]Add > Name : Ip (selected) , IPv4
          * External : +]Add > Name : Ip (selected) , IPv4 > SOurce Region [+] Add > Select Any
  
  9.  Host the GlobalProtect Agent on the Portal 
      * Device > GlobalProtect Client > [ ]Check Now > [click] Download (choose Accordingly) > [click] Activate
  
  10. Create Security Policy Rule 
      * Policies > Security > [+] Add (or Edit existing)
        * General : name, tags(optional)
        * Destination : Destination Zone, Destination Address
        * Service/URL Category : Any, Any

  11. Create a No-NAT Rule 
      * Policies > NAT >[+] Add
        * General : Name, tags, NAT Type(ipv4)
        * Original Packet : Source Zone, Destination Zone, Destination Interface (outgoing interface related to Destination Zone), Destination Address (outgoing Interface IP)
        * Translated Packet : None, None
      * Move top
  
  12. Download the GlobalProtect Agent 
      * 
  13. Connect to the External Gateway
      * you might need ```sudo samba-tool user setpassword <user_id>111
  14. View User-ID Information
      ```
      show user ip-user-mapping all

      ```
  15. Disconnect the Connected User 
      * Network > GlobalProtect > GAteways > Remote Users
  
  16. Configure DNS Proxy (for internal users)
      * Network > DNS Proxy > [+]Add
        * Enable(checked), Primary, secondary, interface > [+]Add (ip Address)
  17. Connect to the Internal Gateway
      * 

## Site to site VPN
  1. Configure the Tunnel Interface
      * Network > Interfaces > Tunnel > [+]Add
        * Interface name, subinterface number on 2nd field
        * Config : Virtual Router, Security Zone
        * Ipv4: [+]Add
        * Advanced: Management Profile (if required)
    
  2. Configure the IKE Gateway 
      * Network > Network Profiles > IKE Gateways >[+]Add
        * General : Name, Version (IKEv1 only mode), interface, local IP, local ip type, peer address(other FW IP), pre-shared key
        * Advanced : IKE Crypto Profile > Dropdown New > 
          * Name, DH Group. Authentication, Encryption 
    
  3. Create an IPSec Crypto Profile
      * Network > Network Profiles > IPSec Crypto > [+]Add
        * General : Name, IPSec Protocol, DH Group, Encryption, uthentication, Name,Tunnel Interface ( dropdown list),Type (Auto Key), Address Type (IPv4), IKE Gateway Select (dmz-ike-gateway),IPSec Crypto(AES256-SHA256),Tunnel Monitor,Destination IP, Profile (None) 
        * Proxy ID: [+]Add : Proxy ID (dmz-tunnel-network), Local (IP Network), Remote(IP network), Protocol(Any)

  4. Configure the IPsec Tunnel
      * Network > IPSec Tunnels > [+]Add
  5. Test Connectivity 
      ```
      show vpn ike-sa
      show vpn ipsec-sa tunnel dmz-tunnel:dmz-tunnel-network
      show vpn flow name dmz-tunnel:dmz-tunnel-network
      show running tunnel flow
      ```

## Active/Passive High Availability 
1. Display the HA Widget 
   * Widgets > System > High Availability 

2. Configure the HA Interface 
   * Network > Interfaces > Ethernet > [Select Interface] > Interface Type (HA)

3. Configure Active/Passive HA 
   * Device > High Availability > General : Enable HA(checked), Group ID (must be unique), Mode 9active Passive), Enable Config Sync (checked), peer HA1 IP Address
   * Click the ```Edit``` icon from the Active/Passive Settings panel. > Auto(selected)
   * Edit icon from the Election Settings panel to configure failover behavior : Device Priority(0-255, lowe has priority), preemptive (checked), heartbeat backup (unchecked)
   * Click the Edit icon from the Control Link (HA1) panel to configure the HA1 link : Port(interface), IPv4/IPv6 Address(IP), Netmask
   * Click the Edit icon from the Data Link (HA2) configuration window : Enable Session Synchronization (UNCHECKED)
  
4. Configure HA Monitoring 
   * Device > High Availability > Link and Path Monitoring : Enabled(checked), Failure Condition(Any) > [+] Add (select interface)
   * Link Grouop (panel) > [+] Add : name, enabled(checked)
   * Path Monitoring window : Enabled(checked), Failure Condition(Any) > [+]Add (8.8.8.8)
  
5. Observe the HA Widget 
    * Dashboard



