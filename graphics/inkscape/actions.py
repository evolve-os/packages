#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import autotools, pisitools, shelltools

def setup():
    autotools.autoreconf('-vfi')
    autotools.configure(" \
                         --enable-lcms \
                         --enable-poppler-cairo \
                         --disable-dependency-tracking \
                         --with-python \
                         --with-inkjar \
                         --enable-nls \
                         --with-perl")

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "ChangeLog", "NEWS", "README")
