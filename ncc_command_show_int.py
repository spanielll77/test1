#!/usr/bin/python

# import the ncclient library
from ncclient import manager
import sys
import xml.dom.minidom


# the variables below assume the user is requesting
# access to a Nexus device running in VIRL in the
# DevNet Always On SandBox
# use the IP address or hostname of your Nexus device
HOST = 'nxosv'
# use the NETCONF port for your Nexus device
PORT = 22
# use the user credentials for your Nexus device
USER = 'cisco'
PASS = 'cisco'


# create a main() method
def main():
    """Main method that retrieves the hostname from config via NETCONF (NXOS)."""
    with manager.connect(host=HOST, port=PORT, username=USER, password=PASS,
                         hostkey_verify=False, device_params={'name': 'nexus'},
                         allow_agent=False, look_for_keys=False) as m:
        #commands = ['conf t','int eth1/1','desc abc']
        commands = ['show int eth1/33']
        reply = m.exec_command(commands) 
        print (reply)
if __name__ == '__main__':
    sys.exit(main())
