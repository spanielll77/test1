import pexpect

r1 = pexpect.spawn('/usr/bin/ssh admin@r1', timeout=5)
r1.expect('ssword:')
r1.sendline('1234QWer')
r1.expect('ter1>')
r1.sendline('show clock')
r1.expect('ter1>')
print(r1.before)
# r1.interact()
