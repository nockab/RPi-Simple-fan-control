# 💨 RPi Simple fan control for Raspbian
Very simple python script that runs 5V fan at set temperature for Raspberry Pi Raspbian

## 💾 Hardware Requirements:
- Raspberry Pi model B 2, 3 or 4
- 5v Fan
- transistor КТ315 (Russian transistor or any analogue)
- 1K-ohm resistor

---

## Software Requirements:
- Raspbian

---

## Hardware Installation steps:
- КТ315 transistor has 3 legs - БКЭ:
 1. Leg Б should be connected to 1K-ohm resistor and to GPIO pin number 4
 2. Leg К sould be connected to 5V power supply pin
 3. Leg Э should be connected to ground pin
Reffer to GPIO pinout for your Raspberry Pi

---

## Software Installation steps:
1. ```sudo apt-get update```
2. ```sudo apt-get upgrade```
3. Copy [fan_control.py](https://github.com/nockab/RPi-Simple-fan-control/blob/master/fan_control.py) contents or file to home/pi/ folder
4. Copy [fan_control.sh](https://github.com/nockab/RPi-Simple-fan-control/blob/master/fan_control.sh) contents or file to home/pi/ folder
5. Change fan_control.sh permissions with ```chmod 755 fan_control.sh```
6. Check if script works ```sh fan_control.sh```, it should run. Ctrl-C to stop.
7. Create folder for crontab logs "mkdir logs"
8. Open for edit crontab ```sudo crontab -e``` or ```crontab -e```
9. If asked, select nano option ```2``` (nano is text editor)
10. At the bottom of file paste: ```@reboot sh /home/pi/fan_control.sh >/home/pi/logs/cronlog 2>&1```
11. Open for edit /etc/rc.local by ```sudo nano /etc/rc.local```
12. At the bottom of file paste: ```/home/pi/fan_control.sh &```
13. Exit from nano an save
14. ```sudo reboot```
15. Enjoy!
> ⚠️ If you choose to store fan_control.sh and fan_control.py files in other folder than home/pi/, change paths accordingly and make sure that correct file path is set in fan_control.sh file (you can open and edit it with ```nano fan_control.sh``` command)
