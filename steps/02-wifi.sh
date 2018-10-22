#!/bin/bash

echo "Setting up wifi"

pacman -S iw wpa_supplicant wpa_actiond dialog
WIRELESS_INTERFACE=$(ls /sys/class/net | grep -m 1 wl)
systemctl enable netctl-auto@$WIRELESS_INTERFACE