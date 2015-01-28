#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, pisitools


def setup():
    autotools.rawConfigure("--prefix=/usr")



def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE")
