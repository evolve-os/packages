#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

def build():
    pass

def install():
    autotools.install()
    pisitools.dodoc("README", "COPYING", "ChangeLog")
