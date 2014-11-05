#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    shelltools.system ("rm -rf libtool libtool.m4")
    autotools.autoreconf("-fi")
    autotools.configure("--enable-static-libs \
                         --enable-cplusplus \
                         --enable-large-config \
                         --enable-threads=posix \
                         --with-libatomic-ops=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.doman("%s/usr/share/gc/gc.man" % get.installDIR())
    shelltools.move("%s/usr/share/gc/" % get.installDIR(), "%s/usr/share/doc/bdwgc/" % get.installDIR())
    pisitools.rename("/usr/share/doc/bdwgc/README.linux", "README")
    pisitools.remove("/usr/share/doc/bdwgc/README.*")
    pisitools.dodoc ("ChangeLog")
