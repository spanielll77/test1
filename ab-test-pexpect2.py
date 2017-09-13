import pexpect

r1 = pexpect.spawn('/usr/bin/ssh admin@r1', timeout=5)

# will it work, if we do now wait for 'Password:' prompt?
# r1.expect('ssword:')

r1.sendline('1234QWer')
r1.expect('ter1>')
r1.sendline('show clock')
r1.expect('ter1>')
print(r1.before)

# Calling interact at the end, will tell you where you are in the ping-pong
r1.interact()
