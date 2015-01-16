#!/usr/bin/python

#Created For Evolve OS

from pisi.actionsapi import cmaketools, pisitools


def setup():
    autotools.configure ("--disable-static \
               		--disable-poppler-qt \
               		--disable-gtk-doc-html \
               		--disable-zlib \
               		--disable-gtk-test \
               		--enable-cairo-output \
               		--enable-xpdf-headers \
               		--enable-libjpeg \
               		--disable-libopenjpeg")


def build():
    cmaketools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.dodoc("README", "AUTHORS", "ChangeLog", "NEWS", "README-XPDF", "TODO")
