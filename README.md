# onionomega-mqtt-micropython
Onion Omega 2+ with OLED and Micropython

Create a directory /opt/demo

Add a USB Stick and Mount

Copy the run.sh and receive3.py to that directory.

Reboot

root@bacon:/opt/demo# crontab -e
root@bacon:/opt/demo# /etc/init.d/cron restart
root@bacon:/opt/demo# crontab -l
*/1 * * * * /opt/demo/run.sh

