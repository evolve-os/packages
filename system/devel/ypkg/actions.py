#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, shelltools

def install():
    shelltools.system("DESTDIR=%s ./install.sh" % get.installDIR())
