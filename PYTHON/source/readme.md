# Activity Notes

## Lecture Materials
* Python basics and python Notebook excercise at [labWork\Module1](../module1/).

## Enable ```virtualenv```

### This is for Windows setup (School Lab)
* Use virtual environment to preserve local environment!
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
* Use virtual enviromment to avoid messing your current Python Environment
  ```bash
  # pip3 install virtualenv
  # virtualenv jupyterlab
  # source mypython/bin/activate
  ...
  # deactivate
  ```
  or
  ```bash
  # mypython/bin/activate
  ```

## Install JupyterLab
* Activate your virtual environment before running or installing
  ```bash
  # pip install jupyterlab
  # jupyter lab
  # jupyter notebook
  ```

## Required Modules
* Build ```requirements.txt``` file
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
