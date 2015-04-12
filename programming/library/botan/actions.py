#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import pisitools, shelltools, autotools, get

def setup():
	shelltools.system("python configure.py")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())
