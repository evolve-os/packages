#!/usr/bin/python

#Created For Evolve OS

from pisi.actionsapi import cmaketools, pisitools


def setup():
    cmaketools.configure()


def build():
    cmaketools.make()


def install():
    cmaketools.install()

    pisitools.dodoc("AUTHORS", "COPYING")
