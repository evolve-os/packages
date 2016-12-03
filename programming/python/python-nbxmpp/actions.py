#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import pythonmodules, pisitools


def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.dodoc("ChangeLog", "COPYING")
