import sys,pexpect,getpass,time

username = raw_input("Username: ")
password = getpass.getpass()

routerFile = open('devicelist', 'r')
routers = [i for i in routerFile]
for router in routers:
    try:
        child = pexpect.spawn ('ssh', [router.strip()])
#        child.expect(['[uU]sername:', '[lL]ogin:'], timeout=3)
#        child.sendline(username)
        child.expect('[pP]assword:')
        child.sendline(password)
        software = child.expect([ '>'], 6)
        print ("Logging into " + router.strip())
    except:
        print "\nCould not log in to " + router.strip()
    pass
    commandlist = 'junos'
    commands = open(commandlist, 'r')
    for command in commands:
        command.strip()
        child.sendline(command.strip())
        child.expect(['>'],20)
##	child.interact()
        print child.before
