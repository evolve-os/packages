#!/usr/bin/python

from pisi.actionsapi import pisitools,shelltools


def setup():
    shelltools.system("ar xf atom-amd64.deb")
    shelltools.system("tar xvf data.tar.gz")

def install():
    pisitools.insinto("/", "usr")
