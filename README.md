# RPi Simple fan control
Very simple python script that powers on fan at set temperature for Raspberry Pi

## Hardware Requirements:
- Raspberry Pi model B 2 or 3
- 5v Fan
- transistor КТ315
- 1K-ohm resistor

## Software Requirements:
- Raspbian

## Hardware Installation steps:
- КТ315 transistor has 3 legs - БКЭ
- Leg Б should be connected to 1K-ohm resistor and to GPIO pin number 4
- Leg К sould be connected to 5V power supply pin
- Leg Э should be connected to ground pin
Reffer to GPIO pinout for RPi 2/3

## Software Installation steps:
- ```sudo apt-get update```
- ```sudo apt-get upgrade```
- Copy [fan_control.py](https://github.com/nockab/RPi-Simple-fan-control/blob/master/fan_control.py) contents or file to home/pi/ folder
- Copy [fan_control.sh](https://github.com/nockab/RPi-Simple-fan-control/blob/master/fan_control.sh) contents or file to home/pi/ folder
- Change fan_control.sh permissions with ```chmod 755 fan_control.sh```
- Check if script works ```sh fan_control.sh```, it should run. Ctrl-C to stop.
- Create folder for crontab logs "mkdir logs"
- Edit crontab ```sudo crontab -e```
- Select nano option ```2```
- At the bottom of file paste:
- ```@reboot sh /home/pi/fan_control.sh >/home/pi/logs/cronlog 2>&1```
- ```sudo reboot```
- Enjoy!
