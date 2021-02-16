name = "tradigitools"
version = "1.5-ta.0.1.0"
build_command = "python {root}/rez_build.py"
authors=["kiki"]

from rez.system import system


private_build_requires = [
	"maya_devkit",
	"python-2.7",
]

if system.platform == "windows":
	private_build_requires += ["visual_studio"]
	print("+ Adding visual_studio to private_build_requires")

## kiki note: if you don't do this it'll crash on build
del system

requires = [
	"maya",
]


# Release this as an external package
with scope("config") as c:
	print("Checking scope...")
	import sys
	if sys.platform.startswith("win"):
		c.release_packages_path = "R:/ext"
		print("\t + Windows: {}".format(c.release_packages_path))
	elif sys.platform == "darwin":
		c.release_packages_path = "/Volumes/r/ext"
	else:
		c.release_packages_path = "/r/ext"


def commands():
	env["MAYA_MODULE_PATH"].append("{root}")
	env["TRADIGITOOLS_VERSION"] = this.version
