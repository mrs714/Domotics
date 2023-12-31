# For the NAS control system, i'll be using a python library, synology-api, which is a wrapper for the Synology DSM API.
from synology_api import filestation, downloadstation

import subprocess
import sys
from flask import jsonify

sys.path.append('../')
from constants import NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD

# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will log in automatically 
# NOTE: for Filestation and Downloadstation only has been added interactive_output=True,
# It can be omitted and initiate the wrapper with the below ove code

fl = filestation.FileStation(NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)

fl.get_info()

dwn = downloadstation.DownloadStation(NAS_IP, NAS_PORT, NAS_USERNAME, NAS_PASSWORD, secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)

dwn.get_info()

def get_nas_info():
    return fl.get_info()

# Is the NAS turned on?
# If yes, fetch info