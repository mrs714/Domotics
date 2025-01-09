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
#fl.get_info()

#dwn = downloadstation.DownloadStation(NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
# I don't have this installed
#dwn.get_info()

class NAS_handler:

    def __init__(self):
        self.syno = None

    def setup_nas_connection(self):
        """
        Setup the connection to the NAS.
        
        Returns:
        - True if the connection was successful.
        - False if the connection failed.
        """
        
        try:
            self.syno = SysInfo(NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
            return True
        except Exception as e:
            print(f"Error setting up NAS connection: {e}")
            return False

    def get_system_overview(self):
        """
        Get an overview of the NAS system.
        Must have a successful connection to the NAS.
        """

        if self.syno is None:
            print("Error: No connection to NAS.")
            return None


        overview = {}

        try:
            # General System Info
            overview['System Info'] = self.syno.get_system_info()
            overview['DSM Info'] = self.syno.dsm_info()
            overview['CPU Temperature'] = self.syno.get_cpu_temp()
            overview['System Utilization'] = self.syno.get_all_system_utilization()

            # Storage Info
            overview['Storage'] = self.syno.storage()
            overview['Disk List'] = self.syno.disk_list()
            overview['Volume Info'] = self.syno.get_volume_info()

            # Network Info
            overview['Network Status'] = self.syno.network_status()
            overview['QuickConnect'] = self.syno.quickconnect_info()
            overview['DDNS Info'] = {
                'Records': self.syno.ddns_record_info(),
                'External IP': self.syno.ddns_external_ip()
            }

            # File Services
            overview['SMB Status'] = self.syno.fileserv_smb()
            overview['AFP Status'] = self.syno.fileserv_afp()
            overview['Shared Folders'] = self.syno.shared_folders_info()

            # Security and Notifications
            overview['Security Scan'] = self.syno.get_security_scan_info()
            overview['Notifications'] = {
                'Email': self.syno.notification_mail_conf(),
                'SMS': self.syno.notification_sms_conf()
            }

            # User and Group Info
            overview['Users'] = self.syno.get_user_list()
            overview['Password Policy'] = self.syno.password_policy()

            # Processes and Logs
            overview['Running Processes'] = self.syno.process()
            overview['Latest Logs'] = self.syno.latest_logs()

        except Exception as e:
            print(f"Error fetching system overview: {e}")

        self.latest_overview = overview
    
    def get_processed_overview(self):
        
        nas_data = self.latest_overview
        info = {}

        # System Info
        system_info = nas_data.get('System Info', {}).get('data', {})
        info['System'] = {
            'Model': system_info.get('model', 'Unknown'),
            'Serial Number': system_info.get('serial', 'Unknown'),
            'Firmware Version': system_info.get('firmware_ver', 'Unknown'),
            'Uptime': system_info.get('up_time', 'Unknown'),
            'Temperature': system_info.get('sys_temp', 'Unknown'),
            'RAM (MB)': system_info.get('ram_size', 'Unknown'),
        }

        # CPU Metrics
        utilization = nas_data.get('System Utilization', {})
        cpu = utilization.get('cpu', {})
        info['CPU'] = {
            'Model': system_info.get('cpu_family', 'Unknown'),
            'Cores': system_info.get('cpu_cores', 'Unknown'),
            'Clock Speed (MHz)': system_info.get('cpu_clock_speed', 'Unknown'),
            '1min Load (%)': cpu.get('1min_load', 'Unknown'),
            '5min Load (%)': cpu.get('5min_load', 'Unknown'),
            '15min Load (%)': cpu.get('15min_load', 'Unknown'),
            'Utilization': {
                'User (%)': cpu.get('user_load', 'Unknown'),
                'System (%)': cpu.get('system_load', 'Unknown'),
                'Other (%)': cpu.get('other_load', 'Unknown'),
            },
        }

        # Storage Metrics
        storage = nas_data.get('Storage', {}).get('data', {})
        disks = storage.get('disks', [])
        volumes = storage.get('volumes', [])
        info['Storage'] = {
            'Disks': [
                {
                    'Name': disk.get('name', 'Unknown'),
                    'Model': disk.get('model', 'Unknown'),
                    'Health': disk.get('status', 'Unknown'),
                    'Temperature (°C)': disk.get('temp', 'Unknown'),
                    'Capacity (Bytes)': disk.get('size_total', 'Unknown'),
                }
                for disk in disks
            ],
            'Volumes': [
                {
                    'Name': volume.get('id', 'Unknown'),
                    'Total Size (Bytes)': volume.get('size', {}).get('total', 'Unknown'),
                    'Used (Bytes)': volume.get('size', {}).get('used', 'Unknown'),
                    'File System': volume.get('fs_type', 'Unknown'),
                    'Status': volume.get('status', 'Unknown'),
                }
                for volume in volumes
            ],
        }

        # Network Metrics
        network = nas_data.get('Network Status', {}).get('data', {})
        info['Network'] = {
            'Hostname': network.get('server_name', 'Unknown'),
            'IP Address': network.get('gateway_info', {}).get('ip', 'Unknown'),
            'Gateway': network.get('gateway', 'Unknown'),
            'External IP': nas_data.get('DDNS Info', {}).get('External IP', {}).get('data', [{}])[0].get('ip', 'Unknown'),
        }

        # Shared Folders
        shared_folders = nas_data.get('Shared Folders', {}).get('data', {}).get('shares', [])
        info['Shared Folders'] = [folder.get('name', 'Unknown') for folder in shared_folders]

        # Notifications
        notifications = nas_data.get('Notifications', {}).get('Email', {}).get('data', {})
        info['Notifications'] = {
            'Sender': notifications.get('sender_mail', 'Unknown'),
            'Alert Levels': notifications.get('template_config', {}).get('default_enabled_rule_level', 'Unknown'),
        }

        # Top Processes
        processes = nas_data.get('Running Processes', {}).get('data', {}).get('process', [])
        info['Top Processes'] = [
            {
                'Command': process.get('command', 'Unknown'),
                'CPU (%)': process.get('cpu', 'Unknown'),
                'Memory (KB)': process.get('mem', 'Unknown'),
            }
            for process in sorted(processes, key=lambda x: x.get('cpu', 0), reverse=True)[:5]
        ]

        self.processed_overview = info
    
    def display_info(self):
        for category, details in self.processed_overview.items():
            print(f"=== {category} ===")
            if isinstance(details, dict):
                for key, value in details.items():
                    print(f"{key}: {value}")
            elif isinstance(details, list):
                for item in details:
                    print(item)
            print()