#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())


def setup():
    autotools.configure("--disable-static --disable-webapps")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
