#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by: python.exe -m py2exe mygame.py -O -W setup.py


import platform
import os
from distutils.core import setup
import py2exe

class Target(object):
    '''Target is the baseclass for all executables that are created.
    It defines properties that are shared by all of them.
    '''
    def __init__(self, **kw):
        self.__dict__.update(kw)

        # the VersionInfo resource, uncomment and fill in those items
        # that make sense:

        # The 'version' attribute MUST be defined, otherwise no versioninfo will be built:
        # self.version = "1.0"

        # self.company_name = "Company Name"
        # self.copyright = "Copyright Company Name © 2013"
        # self.legal_copyright = "Copyright Company Name © 2013"
        # self.legal_trademark = ""
        # self.product_version = "1.0.0.0"
        # self.product_name = "Product Name"

        # self.private_build = "foo"
        # self.special_build = "bar"

    def copy(self):
        return Target(**self.__dict__)

    def __setitem__(self, name, value):
        self.__dict__[name] = value

RT_BITMAP = 2
RT_MANIFEST = 24

# A manifest which specifies the executionlevel
# and windows common-controls library version 6

manifest_template = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="*"
    name="%(prog)s"
    type="win32"
  />
  <description>%(prog)s</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="%(level)s"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="*"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>
'''



mygame = Target(
    script = 'mygame.py',
    dest_base = 'MyGame', # 실행파일이름
    icon_resourcess = [(1,r"pico2d.ico")],
    other_resources = [(RT_MANIFEST, 1, (manifest_template % dict(prog="mygame", level="asInvoker")).encode("utf-8"))]
    )

py2exe_options = dict(
    packages = [],
    optimize=1,
    compressed=True, # uncompressed may or may not have a faster startup
    bundle_files=2,
    dist_dir='dist',
    )

res_etc = './resource/etc/'
res_back = './resource/background/'
res_char = './resource/character/'
res_sound = './sound/'

if platform.architecture()[0] == '32bit':
    sdl_folder = './SDL2/x86/'
else:
    sdl_folder = './SDL2/x64/'

sdl_dlls = [sdl_folder + file_name for file_name in os.listdir(sdl_folder)]

etc_dlls = [res_etc  + file_name for file_name in os.listdir(res_etc )]
back_dlls = [res_back  + file_name for file_name in os.listdir(res_back )]
char_dlls = [res_char + file_name for file_name in os.listdir(res_char)]
sound_dlls = [res_sound + file_name for file_name in os.listdir(res_sound)]

setup(name="name",
      windows=[mygame],
      data_files=[(res_etc , etc_dlls),(res_back , back_dlls),(res_char , char_dlls),(res_sound , sound_dlls),(sdl_folder, sdl_dlls) ],
      zipfile=None,
      options={"py2exe": py2exe_options},
      )