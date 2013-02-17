# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "js-1.8.7/js/src"

def setup():
   autotools.configure("--enable-jemalloc \
                        --enable-readline \
                        --enable-threadsafe \
                        --with-system-nspr \
                        --enable-system-ffi ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")
    
    pisitools.insinto("/usr/include/js", "../public/*.h")
    shelltools.cd("../") 
    pisitools.insinto("/usr/include/mozilla", "../mfbt/*.h")

