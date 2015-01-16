#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import get, autotools, shelltools, pisitools


def setup():
    #pisitools.dosed("src/widgets/desktop-widget.h", "commands_toolbox,", "commands_toolbox")
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
    #/usr/share/icons/hicolor/icon-theme.cache from dia package 
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "ChangeLog", "NEWS", "README")
