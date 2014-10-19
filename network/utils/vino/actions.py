#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, pisitools


def setup():
    autotools.configure()


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog")
