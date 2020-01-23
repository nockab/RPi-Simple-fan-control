# 💨 RPi Simple fan control for Raspbian
Very simple python script that runs 5V fan at set temperature for Raspberry Pi Raspbian

## 💾 Hardware Requirements:
- Raspberry Pi model B 2, 3 or 4
- 5v Fan
- transistor КТ315 (Russian transistor or any analogue)
- 1K-ohm resistor

## Software Requirements:
- Raspbian

## Hardware Installation steps:
- КТ315 transistor has 3 legs - БКЭ:
 - Leg Б should be connected to 1K-ohm resistor and to GPIO pin number 4
 - Leg К sould be connected to 5V power supply pin
 - Leg Э should be connected to ground pin
Reffer to GPIO pinout for your Raspberry Pi

## Software Installation steps:
- ```sudo apt-get update```
- ```sudo apt-get upgrade```
- Copy [fan_control.py](https://github.com/nockab/RPi-Simple-fan-control/blob/master/fan_control.py) contents or file to home/pi/ folder
- Copy [fan_control.sh](https://github.com/nockab/RPi-Simple-fan-control/blob/master/fan_control.sh) contents or file to home/pi/ folder
- Change fan_control.sh permissions with ```chmod 755 fan_control.sh```
- Check if script works ```sh fan_control.sh```, it should run. Ctrl-C to stop.
- Create folder for crontab logs "mkdir logs"
- Edit crontab ```sudo crontab -e``` or ```crontab -e```
- If asked, select nano option ```2``` (nano is text editor)
- At the bottom of file paste:
- ```@reboot sh /home/pi/fan_control.sh >/home/pi/logs/cronlog 2>&1```
- Edit /etc/rc.local by ```sudo nano /etc/rc.local```
- At the bottom of file paste:
- ```/home/pi/fan_control.sh &```
- Exit from nano an save
- ```sudo reboot```
- Enjoy!
- ⚠️ If you choose to store fan_control.sh and fan_control.py files in other folder than home/pi/, change paths accordingly and make sure that correct file path is set in fan_control.sh file (you can open and edit it with ```nano fan_control.sh``` command)
