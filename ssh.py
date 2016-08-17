import os
import pexpect
import stat

import pxssh
import getpass
def command(s,c):
    s.sendline (c)
    s.prompt()
    print type(s.before)
    print s.

s = pxssh.pxssh()
s.login ('115.28.207.130', 'root', "fangyc111'")

command(s,"ls")


s.logout()
