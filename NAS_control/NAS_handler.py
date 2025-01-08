# For the NAS control system, i'll be using a python library, synology-api, which is a wrapper for the Synology DSM API.
from synology_api.core_sys_info import SysInfo

import subprocess
import sys
from flask import jsonify

sys.path.append('../')
from constants import NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD

# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will log in automatically 
# NOTE: for Filestation and Downloadstation only has been added interactive_output=True,
# It can be omitted and initiate the wrapper with the below ove code

#fl = filestation.FileStation(NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
syno = SysInfo(NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
#fl.get_info()

#dwn = downloadstation.DownloadStation(NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
# I don't have this installed
#dwn.get_info()

def get_system_overview():
    overview = {}

    try:
        # General System Info
        overview['System Info'] = syno.get_system_info()
        overview['DSM Info'] = syno.dsm_info()
        overview['CPU Temperature'] = syno.get_cpu_temp()
        overview['System Utilization'] = syno.get_all_system_utilization()

        # Storage Info
        overview['Storage'] = syno.storage()
        overview['Disk List'] = syno.disk_list()
        overview['Volume Info'] = syno.get_volume_info()

        # Network Info
        overview['Network Status'] = syno.network_status()
        overview['QuickConnect'] = syno.quickconnect_info()
        overview['DDNS Info'] = {
            'Records': syno.ddns_record_info(),
            'External IP': syno.ddns_external_ip()
        }

        # File Services
        overview['SMB Status'] = syno.fileserv_smb()
        overview['AFP Status'] = syno.fileserv_afp()
        overview['Shared Folders'] = syno.shared_folders_info()

        # Security and Notifications
        overview['Security Scan'] = syno.get_security_scan_info()
        overview['Notifications'] = {
            'Email': syno.notification_mail_conf(),
            'SMS': syno.notification_sms_conf()
        }

        # User and Group Info
        overview['Users'] = syno.get_user_list()
        overview['Password Policy'] = syno.password_policy()

        # Processes and Logs
        overview['Running Processes'] = syno.process()
        overview['Latest Logs'] = syno.latest_logs()

    except Exception as e:
        print(f"Error fetching system overview: {e}")

    return overview

# Usage
overview = get_system_overview()
for key, value in overview.items():
    print(f"{key}:\n{value}\n")


# Is the NAS turned on?
# If yes, fetch info

print(get_system_overview())