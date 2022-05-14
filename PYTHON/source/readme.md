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
- [Activity 5](#activity-5)
  - [Objectives](#objectives)
  - [Install Required Modules for excercises](#install-required-modules-for-excercises)

<!-- /TOC -->
<br />
<hr>

## Lecture Materials
* Python basics and python Notebook excercise at [labWork\Module1](../module1/).


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


## Activity 5
### Objectives
* Setup and build environment for lab exercises
* **Import OVA** (Open Virtualization Format) file **CISCO IOS-XE** to vitualbox. **CISCO IOS-XE** is a cisco device simulator that can be accessed from a real network.
* Install [Postman](https://www.postman.com/). I also use [Insomia](https://insomnia.rest/download).
* Install [JSONView](https://chrome.google.com/webstore/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc) on your browser ( I use chrome)
* Install [putty](https://www.putty.org/)
* Install [virtualbox](https://www.virtualbox.org/)
 
### Install Required Modules for excercises
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

