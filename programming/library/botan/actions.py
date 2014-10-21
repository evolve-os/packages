#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import pisitools, shelltools, autotools, get

def setup():
	shelltools.system("./configure.py --prefix=/usr --includedir=/usr/include --libdir=/usr/lib --docdir=/usr/share/doc")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.domove ("/bin", "/usr/")
