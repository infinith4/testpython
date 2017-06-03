#!/usr/bin/python

from __future__ import with_statement
from daemon import DaemonContext
# Fedoraの場合
from daemon.pidfile import PIDLockFile
# Fedora以外の場合
from daemon.pidlockfile import PIDLockFile


dc = DaemonContext(
    pidfile=PIDLockFile('./tmp/lock'),
    stderr=open('./tmp/lock', 'w+')
)

with dc:
    print("test")
