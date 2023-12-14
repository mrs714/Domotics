#!/bin/bash

# Get the IP address from the command line argument
MAIN_PC_IP=$1

# Function to send ping and check the response
send_ping() {
    ping_result=$(ping -c 1 -W 1 $MAIN_PC_IP)
    if [ $? -eq 0 ]; then
        echo "Main PC is ON"
        return 0  # Success (main PC is ON)
    else
        echo "Main PC is OFF"
        return 1  # Failure (main PC is OFF)
    fi
}

# Call the send_ping function
send_ping