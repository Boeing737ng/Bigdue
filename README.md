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
    - (Windows) \Scripts\activate
  3. pip install -r requirements.txt
  4. Do something
  5. deactivate virtual environments
    - (Linux/OSX) deactivate
    - (Windows) \Scripts\deactivate

## Installation

### Windows
  #### 0. Clone Bigdue Project
    - $ git clone https://github.com/Boeing737ng/Bigdue.git

  #### 1. Install python3, Download WinPcap, WinPcap Dev Pack
    - python3 : https://www.python.org/
    - WinPcap : https://www.winpcap.org/install/default.htm
    - WinPcap Dev Pack : https://www.winpcap.org/devel.htm

  #### 2. Install Maxmind db
    - GeoLite2 City DB : https://dev.maxmind.com/geoip/geoip2/geolite2/
    - Copy the installed GeoLite2-City.mmdb file under geolite folder
    
  #### 3. Create virtual environments
    - $ python -m venv ./

  #### 4. Download and copy WinPcap Devs files to venv
    - Copy all the file in the "Include" folder which is in Winpcap dev pack to "Include" folder
    - Copy Packet.lib and wpcap.lib in Winpcap dev pack/"Lib" to "Lib" folder. If you are using 64bits, copy the file from x64 folder
    
  #### 5. Activate virtual environments
    In cmd
    - $ cd Scripts
    - $ activate.bat

    In git bash
    - $ source Scripts/activate
    
  #### 6. Install requirements modules
    - $ pip install -r requirements.txt

  #### 7. Enjoy
    - $ python routes.py
    
### Mac OS / Linux
  #### 0. Clone Bigdue Project
    - $ git clone https://github.com/Boeing737ng/Bigdue.git

  #### 1. Install python3
    - python3 : https://www.python.org/

  #### 2. Install Maxmind db
    - GeoLite2 City DB : https://dev.maxmind.com/geoip/geoip2/geolite2/
    - Copy the installed GeoLite2-City.mmdb file under geolite folder

  #### 3. Create virtual environments
    - $ python3 -m venv ./

  #### 4. Activate virtual environments
    - $ source ./bin/activate

  #### 5. Install requirements modules
    - $ pip3 install -r requirements.txt

  #### 6. Enjoy
    - $ python3 routes.py