#!/usr/bin/env python


import sys
# Load the wrapper module, it's linked against FBInk, so the dynamic loader will take care of pulling in the actual FBInk library
from _fbink import ffi, lib as FBInk
import KIP
import time


# And now we're good to go! Let's print "Hello World" in the center of the screen...
# Setup the config...
fbink_cfg = ffi.new("FBInkConfig *")
fbink_cfg.is_centered = True
fbink_cfg.is_halfway = True


# Open the FB...
fbfd = FBInk.fbink_open()
FBInk.fbink_init(fbfd, fbink_cfg)
#FBInk.fbink_close(fbfd)




touchPath = "/dev/input/event1"
t = KIP.inputObject(touchPath, 1080, 1440)
FBInk.fbink_print(fbfd, b"Test ! Have Fun... Starting in 5 secs", fbink_cfg)
FBInk.fbink_close(fbfd)
time.sleep(5)
fbfd = FBInk.fbink_open()
FBInk.fbink_print(fbfd, b"Started", fbink_cfg)
FBInk.fbink_close(fbfd)

while True:
	(x,y,err) = t.getInput()
	print(x,y)
	fbfd = FBInk.fbink_open()
	FBInk.fbink_print(fbfd, str(x) + " - " + str(y), fbink_cfg)