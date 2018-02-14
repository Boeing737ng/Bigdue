# Bigdue

## Network Packet Analysis

## Project
  1. Visualization
  2. Usage

## Usage methods
  0. clone git repository
  1. python -m venv ./
  2. activate virtual environments
    - (Linux/OSX) source ./bin/activate
    - (Windows) \Script\activate
  3. pip install -r requirements.txt
  4. Do something
  5. deactivate virtual environments
    - (Linux/OSX) deactivate
    - (Windows) \Script\deactivate

## Installation

### Windows
  #### 0. Clone Bigdue Project
    - $ git clone https://github.com/Boeing737ng/Bigdue.git

  #### 1. Install python3, Download WinPcap, WinPcap Dev Pack
    - python3 : https://www.python.org/
    - WinPcap : https://www.winpcap.org/install/default.htm
    - WinPcap Dev Pack : https://www.winpcap.org/devel.htm

  #### 2. Install virtual environments
    - $ pip install virtualenv
  
  #### 3. Create virtual environments
    - $ virtualenv venv

  #### 4. Download and copy WinPcap Devs files to venv
    - Copy all the file in the include folder which is in Winpcap dev pack to include folder in venv
    - Copy Packet.lib and wpcap.lib in Winpcap dev pack/lib to lib folder in venv. If you are using 64bits, copy the file from x64 folder
    
  #### 5. Activate virtual environments
    - $ source venv/Scripts/activate
    
  #### 6. Install requirements modules
    - $ pip install -r requirements.txt

  #### 7. Enjoy
    - $ python routes.py

### Mac OS
  #### 0. Clone Bigdue Project
    - $ git clone https://github.com/Boeing737ng/Bigdue.git

  #### 1. Install python3
    - python3 : https://www.python.org/

  #### 2. Install virtual environments
    - $ pip3 install virtualenv
  
  #### 3. Create virtual environments
    - $ virtualenv venv

  #### 4. Activate virtual environments
    - $ source venv/bin/activate

  #### 5. Install requirements modules
    - $ pip3 install -r requirements.txt

  #### 7. Enjoy
    - $ python3 routes.py