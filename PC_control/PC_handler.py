import subprocess
import sys
from flask import jsonify

sys.path.append('../')
from constants import PC_IP

def send_ping_to_main_pc():
    main_pc_script = "./PC_control/ping.sh"  # Adjust the path accordingly

    try:
        # Run the Bash script with the IP address as an argument
        process = subprocess.Popen([main_pc_script, PC_IP], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode == 0:
            print("Main PC is ON")
            return jsonify({"status": "ON", "ip": PC_IP})
        else:
            print("Main PC is OFF")
            return jsonify({"status": "OFF", "ip": PC_IP})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "failed", "ip": PC_IP})