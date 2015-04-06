#!/usr/bin/python
# -*- coding: utf-8 -*-
#
KVERSION = "3.19.3"

from pisi.actionsapi import kerneltools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

NoStrip = ["/boot"]

shelltools.export("KBUILD_BUILD_USER", "evolveos")
shelltools.export("KBUILD_BUILD_HOST", "beta")
shelltools.export("PYTHONDONTWRITEBYTECODE", "1")
shelltools.export("HOME", get.workDIR())

cpupower_arch = get.ARCH().replace("i686", "i386")

def setup():
    kerneltools.configure()

def build():
    kerneltools.build(debugSymbols=False)

def install():
    # pisi needs patching to check if the links exist, before it removes them
    pisitools.dodir("/lib/modules/%s" % KVERSION)
    shelltools.echo("%s/lib/modules/%s/source" % (get.installDIR(), KVERSION), "mustFix")
    shelltools.echo("%s/lib/modules/%s/build" % (get.installDIR(), KVERSION), "mustFix")

    kerneltools.install()

    # Install kernel headers needed for out-of-tree module compilation
    kerneltools.installHeaders()

    kerneltools.installLibcHeaders()


    # Generate some module lists to use within mkinitramfs
    shelltools.system("./generate-module-list %s/lib/modules/%s" % (get.installDIR(), kerneltools.__getSuffix()))
