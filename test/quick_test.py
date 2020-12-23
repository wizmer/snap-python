import snap
version = snap.Version
i = snap.TInt(5)
assert i == 5, "*** ERROR, no working Snap.py was found on your computer"
print("SUCCESS, your version of Snap.py is %s" % (version))
