
# Paraphrasing after: https://pynet.twb-tech.com/blog/automation/netmiko.html, by Kirk Byers

# Assumption is r1 has enable prompt:
# line vty 0 5
#    no privil level 15
# hostname Router1


from netmiko import ConnectHandler

cisco_r1 = { 'device_type': 'cisco_ios',
             'ip': 'r2',
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

r1.send_command("show clock")
#  '*11:18:51.938 UTC Sun Sep 10 2017\nXX>'

# Netmiko automatically discovered changed prompt!
