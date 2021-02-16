#!/usr/local/bin/python

from __future__ import print_function

import os
import shutil
import sys


source_folder = os.environ["REZ_BUILD_SOURCE_PATH"].replace("\\","/")
dest_folder   = os.environ["REZ_BUILD_INSTALL_PATH"].replace("\\","/")

if os.path.exists(dest_folder):
    shutil.rmtree(dest_folder, ignore_errors=True)

source_folder_path = os.path.join(source_folder, "module")
dest_folder_path   = os.path.join(dest_folder, "module")

os.chdir(source_folder)

for folder in "module", "build":
    to_remove = os.path.join(source_folder, folder)
    if os.path.exists(to_remove):
        shutil.rmtree(to_remove, ignore_errors=True)
        print("+ Cleaned old path: {}".format(to_remove))


## cmake build
build_commands = [
    "mkdir build",
    "pushd build",
    "cmake {generator} -DCMAKE_GENERATOR_PLATFORM=x64 ..",
    "popd",
    "cmake --build build --target INSTALL --config Release",
]

command = "&&".join(build_commands)
generator = ""

if sys.platform.startswith("win"):
    command = 'cmd /c ' + command
    generator = "Visual Studio 15.0 2017 Win64"

os.system(command.format(generator=generator))

try:
    if os.path.exists(dest_folder_path):
        shutil.rmtree(dest_folder_path, ignore_errors=True)
    shutil.copytree(source_folder_path, dest_folder_path)
    print("Copied folder: {}".format(dest_folder_path))
    target_module_file = os.path.join(dest_folder, "tradigitools.mod")
    shutil.copyfile(os.path.join(source_folder, "tradigitools.mod"),
                    target_module_file)
    print("Set up module file: {}".format(target_module_file))
    target_user_setup = os.path.join(dest_folder_path, "scripts", "userSetup.py")
    shutil.copyfile(os.path.join(source_folder, "userSetup.py"),
                    target_user_setup)
    print("Copied userSetup.py: {}".format(target_user_setup))

except Exception as e:
    print(" - {}".format(e))
    pass



