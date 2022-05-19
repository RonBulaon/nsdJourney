<h1>Activity Notes</h1>

<h3>Table of Contents</h3>
<!-- TOC -->

- [Lecture Materials](#lecture-materials)
- [Enable ```virtualenv```](#enable-virtualenv)
  - [This is for Windows setup (School Lab)](#this-is-for-windows-setup-school-lab)
  - [For Mac (Daily Driver)](#for-mac-daily-driver)
- [IDE and others](#ide-and-others)
  - [Replit](#replit)
  - [Install JupyterLab](#install-jupyterlab)
- [Class 5](#class-5)
  - [Objectives](#objectives)
  - [Install Required Modules for Exercises](#install-required-modules-for-exercises)
- [Class 6](#class-6)
  - [Activity : 2.2 Lab - CLI Automation with Python using netmiko](#activity--22-lab---cli-automation-with-python-using-netmiko)
    - [Objectives](#objectives-1)
    - [Solution : ```class6_netmiko.py```](#solution--class6_netmikopy)
  - [Activity : 2.3 Lab - Explore YANG models using the pyang tool](#activity--23-lab---explore-yang-models-using-the-pyang-tool)
- [Class 7](#class-7)
  - [Activity : 2.5 Lab - RESTCONF with Python](#activity--25-lab---restconf-with-python)
    - [Objectives](#objectives-2)
    - [Solution 1 : ```lab 2.5.py```](#solution-1--lab-25py)
    - [Solution 2 : ```lab 2.5 part2.py```](#solution-2--lab-25-part2py)
- [Class 8](#class-8)
  - [Activity : 2.7 Lab - NETCONF with Python List Capabilities](#activity--27-lab---netconf-with-python-list-capabilities)
    - [Objectives](#objectives-3)
    - [Solution : ```lab27.py```](#solution--lab27py)
  - [Activity : 2.8 Lab - NETCONF with Python Device Configuration](#activity--28-lab---netconf-with-python-device-configuration)
    - [Objectives](#objectives-4)
    - [Solution : ```lab2.8py```](#solution--lab28py)
  - [Activity : 2.9 Lab - NETCONF with Python Get Operational Data](#activity--29-lab---netconf-with-python-get-operational-data)
    - [Objectives](#objectives-5)
    - [Solution : ```lab29.py```](#solution--lab29py)
- [Replit Exercises](#replit-exercises)

<!-- /TOC -->
<br />
<hr>

## Lecture Materials
* Python basics and python Notebook excercise at [labWork\Module1](../module1/).
* Check out http://developer.cisco.com 
* Note : COurse focuses on *introducing* Softwre Defined Network.


## Enable ```virtualenv```
* Use virtual environment to preserve local environment. **Optional but recommended**.


### This is for Windows setup (School Lab)
* Install ```virtualenv```
  ```cmd
  > pip install virtualenv
  ```
* Activate
  ```cmd
  > "C:\Users\CCNA\Desktop\RonOneDrive\OneDrive - University of Winnipeg\pythonModule\venv\Scripts\activate.bat"
  ```
* Deactivate:
  ```cmd
  > "C:\Users\CCNA\Desktop\RonOneDrive\OneDrive - University of Winnipeg\pythonModule\venv\Scripts\deactivate.bat"
  ```

### For Mac (Daily Driver)
* Install, activate and deactivate.
  ```bash
  # pip3 install virtualenv
  # virtualenv jupyterlab
  # source mypython/bin/activate
  ...
  # deactivate
  ```


## IDE and others
### Replit
* [Replit](http://www.replit.com/) is a simple yet powerful online IDE, Editor, Compiler, Interpreter, and REPL. Code, compile, run, and host in 50+ programming languages. (from website)
* Used for some excercises and some test demonstration.

### Install JupyterLab
* Activate your virtual environment before running or installing
  ```bash
  # pip install jupyterlab
  # jupyter lab
  # jupyter notebook
  ```

<br/><br/>

## Class 5
### Objectives
* Setup and build environment for lab exercises
* **Import OVA** (Open Virtualization Format) file **CISCO IOS-XE** to vitualbox. **CISCO IOS-XE** is a cisco device simulator that can be accessed from a real network.
* Install [Postman](https://www.postman.com/). I also use [Insomia](https://insomnia.rest/download).
* Install [JSONView](https://chrome.google.com/webstore/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc) on your browser ( I use chrome)
* Install [putty](https://www.putty.org/)
* Install [virtualbox](https://www.virtualbox.org/)
 
### Install Required Modules for Exercises
* This was not taught during class.
* Build ```requirements.txt``` file. 
  ```bash
  requests
  tabulate
  ncclient
  pyang --no-binary=pyang
  netmiko
  xmltodict
  ```
* Install modules
  ```bash
  # pip install -r requirements.txt
  ```
* Verify installed modules
  ```bash
  # pip freeze
  ```

<br/><br/>

## Class 6
### Activity : 2.2 Lab - CLI Automation with Python using netmiko 
#### Objectives 
  * [Lab Instructions and solutions](../class6/2.2%20Lab%20-%20CLI%20Automation%20with%20Python%20using%20netmiko.pdf)
  * Part 1: Install the netmiko Python module
  * Part 2: Connect to IOS XE’s SSH service using netmiko
  * Part 3: Use netmiko to gather information from the device
  * Part 4: Use netmiko to alter configuration on the device

#### Solution : ```class6_netmiko.py```
  ```python
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
  ```
### Activity : 2.3 Lab - Explore YANG models using the pyang tool 
* [Lab Instructions and solutions](../class6/2.3%20Lab%20-%20Explore%20YANG%20models%20using%20the%20pyang%20tool.pdf)

<br/><br/>

## Class 7
### Activity : 2.5 Lab - RESTCONF with Python
#### Objectives
* [Lab Instructions and solutions](../class7/lab%202.5.py)
* Part 1: RESTCONF basics in Python
* Part 2: Modify interface configuration with RESTCONF in Python

#### Solution 1 : ```lab 2.5.py```
  ```python
  import json
  import requests

  requests.packages.urllib3.disable_warnings()

  api_url = "https://10.128.207.132/restconf/data/ietf-interfaces:interfaces"

  headers = {
      "Accept": "application/yang-data+json", 
      "Content-type":"application/yang-data+json"
  }

  basicauth = ("cisco", "cisco123!")

  resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
  response_json = resp.json()
  # print(response_json)
  print(json.dumps(response_json, indent=4))
  ```

#### Solution 2 : ```lab 2.5 part2.py```
  ```python
  import json
  import requests

  requests.packages.urllib3.disable_warnings()

  api_url = "https://10.128.207.132/restconf/data/ietf-interfaces:interfaces/interface=Loopback99"

  headers = {
      "Accept": "application/yang-data+json", 
      "Content-type":"application/yang-data+json"
  }

  basicauth = ("cisco", "cisco123!")

  yangConfig = {
      "ietf-interfaces:interface": {
          "name": "Loopback99",
          "description": "WHATEVER99",
          "type": "iana-if-type:softwareLoopback",
          "enabled": True,
          "ietf-ip:ipv4": {
              "address": [
                  {
                      "ip": "99.99.99.99",
                      "netmask": "255.255.255.0"
                  }
              ]
          },
          "ietf-ip:ipv6": {}
      }
  }

  # resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
  resp = requests.delete(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
  if(resp.status_code >= 200 and resp.status_code <= 299):
      print("STATUS OK: {}".format(resp.status_code))
  else:
      print("Error code {}, reply: {}".format(resp.status_code, resp.json()))
  ```

<br /><br />

## Class 8
### Activity : 2.7 Lab - NETCONF with Python List Capabilities
#### Objectives
* [Lab Instructions and solutions](../class8/RonAnswered_2.7%20Lab%20-%20NETCONF%20wPython%20List%20Capabilities.pdf)
* Part 1: Install the ncclient Python module
* Part 2: Connect to IOS XE’s NETCONF service using ncclient
* Part 3: List the IOS XE’s capabilities – supported YANG models

#### Solution : ```lab27.py```
  ```python
  from ncclient import manager

  m = manager.connect(
      host="10.128.207.132",
      port=830,
      username="cisco",
      password="cisco123!",
      hostkey_verify=False
  )

  yangModelsToCheck = [
      "Cisco-IOS-XE-voice",
      "Cisco-IOS-XE-cdp",
      "Cisco-IOS-XE-bgp",
      "Cisco-IOS-XE-crypto",
      "Cisco-IOS-XE-eigrp",
      "Cisco-IOS-XE-tunnel",
      "Test-Control",
  ]

  print("# Supported Capabilities (YANG models):")
  for capability in m.server_capabilities:
      supportedYangModel = capability.split('?')[-1].split("&")[0].split('=')[-1]
      if supportedYangModel in yangModelsToCheck:
          print("\t-", supportedYangModel)
  ```

### Activity : 2.8 Lab - NETCONF with Python Device Configuration
#### Objectives
* [Lab Instructions and solutions](../class8/RonAnswered_2.8%20Lab%20-%20NETCONF%20wPython%20Device%20Configuration.pdf)
* Part 1: Retrieve the IOS XE VMs’ existing running configuration
* Part 2: Update the device’s configuration

#### Solution : ```lab2.8py```
  ```python
  from ncclient import manager
  import xml.dom.minidom

  m = manager.connect(
      host="10.128.207.132",
      port=830,
      username="cisco",
      password="cisco123!",
      hostkey_verify=False
  )

  ### Retrieve device 
  netconf_reply = m.get_config(source="running")
  print(netconf_reply)


  ### Retrieve device settings with filter
  netconf_filter = """
  <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
  </filter>
  """

  netconf_reply = m.get_config(source="running", filter=netconf_filter)
  print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )


  ### Change Hostname
  netconf_data = """
  <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <hostname>NEWHOSTNAME</hostname>
    </native>
  </config>
  """

  netconf_reply = m.edit_config(target="running", config=netconf_data)
  print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

  ### Create Loopback Interface
  netconf_data = """
  <config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
    <Loopback>
      <name>100</name>
      <description>TEST1</description>
      <ip>
      <address>
        <primary>
        <address>100.100.100.100</address>
        <mask>255.255.255.0</mask>
        </primary>
      </address>
      </ip>
    </Loopback>
    </interface>
  </native>
  </config>
  """

  netconf_reply = m.edit_config(target="running", config=netconf_data)
  print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


  ### Create loopback with conflicting address
  netconf_data = """
  <config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
    <Loopback>
      <name>111</name>
      <description>TEST1</description>
      <ip>
      <address>
        <primary>
        <address>100.100.100.100</address>
        <mask>255.255.255.0</mask>
        </primary>
      </address>
      </ip>
    </Loopback>
    </interface>
  </native>
  </config>
  """
  netconf_reply = m.edit_config(target="running", config=netconf_data)
  print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
  ```

### Activity : 2.9 Lab - NETCONF with Python Get Operational Data
#### Objectives
* [Lab Instructions and solutions](../class8/RonAnswered_2.9%20Lab%20-%20NETCONF%20wPython%20Get%20Operational%20Data.pdf)
* Part 1: Retrieve the IOS XE VMs’ existing running configuration

#### Solution : ```lab29.py```
  ```python
  from ncclient import manager
  import xml.dom.minidom
  import xmltodict

  m = manager.connect(
      host="10.128.207.132",
      port=830,
      username="cisco",
      password="cisco123!",
      hostkey_verify=False
  )

  netconf_filter = """
  <filter>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
  </filter>
  """

  netconf_reply = m.get(filter = netconf_filter)
  print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

  netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
  for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
      print("Name: {} MAC: {} Input: {} Output {}".format(
                  interface["name"],
                  interface["phys-address"],
                  interface["statistics"]["in-octets"],
                  interface["statistics"]["out-octets"]
        )
      )
  ```
<br /> <br />

## Replit Exercises
* Exercise 1
  ```python
  # Write a Python program that uses three variables. The variables in your program will be country, province, and city. Assign a string value to each one of the variables. Your program should display "Here is an example of a country, a province, and a city." Next, display the value for country, followed by province, and city. Each one of the values should be printed on their own line. Your program will display four lines in total.

  # Put your codes below
  x, y, z = "Canada", "Manitoba", "Winnipeg"
  print(
      'Here is an example of a country, a province, and a city. \n%s \n%s \n%s' %
      (x, y, z))

  ```
* Exercise 2
  ```python
  # Similar output of Exercise 1 but minimize your code to use one print() function only.

  # Put your codes below
  x,y,z = "Canada", "Manitoba", "Winnipeg"
  print('Here is an example of a country, a province, and a city. \n%s \n%s \n%s' % (x,y,z) )
  ```
* Exercise 3
  ```python
  # Create a code that will output exactly the same of the output file.

  # Put your codes below
  print('The','light','sly','fox','jumped','over','the','lazy','dog',sep=('***\n'), end=('***\n'))
  ```
* Exercise 4
  ```python
  # Modify the first line of code in the editor, using the sep and end keywords, to match the expected output. Use the two print() functions in the editor.

  # Don't change anything in the second print() invocation.

  print("Programming","Essentials","in", sep=('***'),end=('...'))
  print("Python")  
  ```
* Exercise 5
  ```python
  #Troubleshoot the following line of code

  print("REST APIs use Uniform Resource Identifiers or (URIs) \nThese are the parts of a URI:")
  print('\nURI = schema "://" authority "/" path [ "?" ] [ "#" fragment ]\n')
  # print("URI = schema "://\" authority "//\" path [ "?" ] [ /"#/" fragment ]\n")
  print("Think of the URI as the location of the data")
  ```
* Exercise 1-15
  ```python
  # Create a Python program that enters and displays the equipment entered. Continually prompt the user for another item until they enter a blank item. After all the items are entered, display the equipment list back to the user.

  # Put your code below
  y = []
  while True:
      x = input("Enter the device hostname. Press <enter> when done: ")
      if len(x):
          y.append(x)
          print("Device added.")
      if x == '':
          print("\nEquipment List:")
          for each in y:
              print(each)
          break
  ```
* Troubleshooting List and Dictionary
  ```python
  # Create a list of the BRICS countries
  country = [ 
              "Brazil", 
              "Russia", 
              "India", 
              "China", 
              "South Africa"
            ]

  """Create a dictionary of BRICS capitals.
  Note that South Africa has 3 capitals. Therefore, we embed a list inside
  the dictionary.
  """

  capitals = {
      "Brazil": "Brasilia",
      "Russia": "Moscow",
      "India": "New Delhi",
      "China": "Beijing",
      "South Africa": [
                          "Pretoria",
                          "Cape Town",
                          "Bloemfontein"
                      ]
            }

  # Print the list and dictionary
  print( country ) # Printing the elements in the country
  print( capitals ) # Printing the key:value pairs in capitals
  """
  What response did you get?
  Why did the list and dictionary contents not print?
  Fix the code and run the script again.
  """

  print(capitals["South Africa"][1]) # Printing the capital Cape Town which is index 1
  """
  Why did you get an error for the 2nd capital of South Africa?
  Hint: Check the syntax for the index value.
  """
  ```
* Troubleshoot a script
  ```python
  '''
  Troubleshoot the Script to Allow User to Add Devices

  1. For the open() function use the mode a, which will allow you to append an item to the devices.txt file.(Note: device.txt will be automatically created when script runs)
  2. Inside a while True: loop, embed an input() function command that asks the user for the new device.
  3. Set the value of the user's input to a variable named newItem.
  4. Use an if statement that breaks the loop if the user types exit and prints the statement "All done!".
  5. Use the command file.write(newItem + “\n”) to add the new user provided device.

  Run and troubleshoot your script until you get output similar to 1.2.6.4.PNG
  '''

  while True:
    newItem = input("Enter device name: ")
    if newItem == "exit":
      print("All done!")
      break
    file = open("devices.txt", "a") 
    file.write(newItem + "\n")
    file.close()
  ```
* Check status of a JSON Request
  ```python
  '''
  Troubleshoot the codes below which will do the following:

  1. Print the constructed URL so that the user can see the exact request made by the application.
  2. Parse the JSON data to obtain the statuscode value
  3. Print the statuscode value and a message if the request is successful. The \n adds a blank line after the message.

  You will need to import two modules from the Python library: requests and urllib.parse. The request module provides functions for retrieving JSON data from a URL.  

  '''

  #Replace 'your_api_key' with your MapQuest API key

  import urllib.parse
  import requests

  main_api = "https://www.mapquestapi.com/directions/v2/route?"
  orig = "Toronto"
  dest = "New York"
  key = 'your_api_key'

  url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
  #(Note: The url value has no error)
  print("URL:", url)

  json_data = requests.get(url).json()
  json_status = json_data["info"]["statuscode"]

  if json_status == 0:
      print("API Status: " + str(json_status) + " = A successful route call.\n")
  ```
* Exercise : 2.4.1.4.0.1
  ```python
  '''
  Click on the 2.4.1.4.01 image to the left.
  Make the necessary changes to the code so that
  it runs without any errors. Once you have completed
  this activity, you can 'Submit' your file.Click on the image
  to the left to see what the output should produce.
  '''
  import requests

  url = "https://w3schools.com/python/demopage.html"
  print(url)
  x = requests.get(url)
  print(x)
  ```
* Exercise : 24.1.4.0.2
  ```python
  '''
  Click on the 24.1.4.02 image to the left.
  Make the necessary changes to the file so that
  it runs without any errors. Once you have completed
  this activity, you can 'Submit' your file. Click on the image
  to the left to see what the output should produce.
  '''
  import requests

  url = "https://mitt.ca"
  print(url)
  httpResponse = requests.head(url)
  print(httpResponse)
  httpStatusCode = httpResponse.status_code
  print(httpStatusCode)
  ```