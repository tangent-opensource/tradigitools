import inspect
import os

from maya import cmds as mc


def tradigitools_setup():
	mc.loadPlugin("tradigitools", quiet=True)
	print("+ tradigitools {} loaded".format(os.environ["TRADIGITOOLS_VERSION"]))

mc.evalDeferred(tradigitools_setup, lp=True)



