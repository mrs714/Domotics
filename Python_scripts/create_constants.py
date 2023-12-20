# Create file constants.py from constants.txt
# You can run this file manually, but it will be run automatically when you run app.py

import os
import sys

def create_constants():
    # Create file constants.py from constants.txt
    path = os.path.dirname(os.path.realpath(__file__))
    path = path.replace("Python_scripts", "")
    path = path + "constants.txt"
    try:
        with open(path, "r") as f:
            lines = f.readlines()
    except:
        print("Error: File constants.txt not found.")
        sys.exit(1)

    path = path.replace("constants.txt", "constants.py")
    try:
        with open(path, "w") as f:
            f.write("\"\"\" \n")
            f.write("    This file will be created automatically from a file constants.txt, by Python_script/create_constants.py.\n")
            f.write("    The file constants.txt must be created manually and must contain the following information:\n")
            f.write("        - PC_IP\n")
            f.write("        - PC_MAC\n")
            f.write("        - NAS_IP\n")
            f.write("        - NAS_PORT\n")
            f.write("        - NAS_USERNAME\n")
            f.write("        - NAS_PASSWORD\n")
            f.write("    Each information must be on a separate line, with no formatting.\n")
            f.write("    Example:\n")
            f.write("        192.192.1.192\n")
            f.write("        01-23-45-67-89-AB\n")
            f.write("        192.192.1.193\n")
            f.write("        5000\n")
            f.write("        admin\n")
            f.write("        password\n")
            f.write("\"\"\"\n")
            f.write("\n")
            f.write("\n")
            f.write("PC_IP = '{}'\n".format(lines[0].strip()))
            f.write("PC_MAC = '{}'\n".format(lines[1].strip()))
            f.write("\n")
            f.write("NAS_IP = '{}'\n".format(lines[2].strip()))
            f.write("NAS_PORT = '{}'\n".format(lines[3].strip()))
            f.write("NAS_USERNAME = '{}'\n".format(lines[4].strip()))
            f.write("NAS_PASSWORD = '{}'\n".format(lines[5].strip()))
            f.write("\n")
            f.write("\n")
    except:
        print("Error: File constants.py could not be created.")
        sys.exit(1)

if __name__ == "__main__":
    create_constants()