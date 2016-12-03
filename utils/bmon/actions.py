#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, pisitools, shelltools


def setup():
    shelltools.system("./autogen.sh --prefix=/usr")
    autotools.configure()


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    
