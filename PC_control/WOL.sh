#!/bin/bash

# MAC address of your main PC
MAIN_PC_MAC=$1

# Function to send Wake-on-LAN packet
wake_up_main_pc() {
    wakeonlan $MAIN_PC_MAC
}

# Run the Wake-on-LAN function
wake_up_main_pc