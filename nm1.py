
# Paraphrasing after: https://pynet.twb-tech.com/blog/automation/netmiko.html, by Kirk Byers

# Assumption is r1 has enable prompt:
# line vty 0 5
#    no privil level 15
# hostname Router1
from datetime import datetime
start_time = datetime.now()
print (format(start_time))

from netmiko import ConnectHandler

cisco_r1 = { 'device_type': 'cisco_ios',
             'ip': 'r1',
             'username': 'cisco',
             'password': 'cisco'
             }

r1 = ConnectHandler(**cisco_r1)

##prompt = r1.find_prompt()
##assert prompt == 'Password:'

x = r1.send_command("show clock")
print(x)
#  '*11:18:51.938 UTC Sun Sep 10 2017'


# make ssh connection to Router1, execute:
# Router1(config)# hostname XX
#

# Now try send_command one more time...
##r1.enable()

#r1.send_command("enable")
r1.send_command("enable",expect_string="Password:")
r1.send_command("cisco",expect_string="#")
#x = r1.send_command("enable")
print(x)
#r1.find_prompt()
## print(r1.send_command("show run"))

prompt = r1.find_prompt()
print(prompt)
r1.config_mode()
prompt = r1.find_prompt()
print(prompt)

x = r1.send_command("show run")
print(x)
#  '*11:18:51.938 UTC Sun Sep 10 2017\nXX>'

# Netmiko automatically discovered changed prompt!
