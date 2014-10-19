#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, pisitools, shelltools

def install():
    shelltools.system("install screenfetch-dev /usr/bin/screenfetch")
    shelltools.system("install screenfetch.1 /usr/share/man/man1/")
    pisitools.dodoc("COPYING", "CHANGELOG")