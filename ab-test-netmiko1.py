
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

prompt = r1.find_prompt()
assert prompt == 'Router2>'
# prompt is equal to 'Router1>'

r1.send_command("show clock")
#  '*11:18:51.938 UTC Sun Sep 10 2017'


# make ssh connection to Router1, execute:
# Router1(config)# hostname XX
#

# Now try send_command one more time...

r1.send_command("show clock")
#  '*11:18:51.938 UTC Sun Sep 10 2017\nXX>'

# Netmiko automatically discovered changed prompt!
# it just that now, the output has a new prompt appended!


prompt = r1.find_prompt()
assert prompt == 'Router1>'
# new prompt is discovered

# However base_prompt still as older...
r1.base_prompt == 'Router1'


r1.send_command("enable")   # hangs!  why?


r1.send_command("enable\ncisco", delay_factor=0.4)
# ''
r1.send_command("show clock")
# 'g "1234QWer"...domain server (255.255.255.255)'

# hangs - router was waiting for our password for enable!
# 1234QWer was buffered, so then it tries to resolve it ...


