# Minimal working example of code that grabs the git hash for a file
#
# TODO:
# 1. Make a tlab_git module
# 2. Checkout gitpython
#
# Other notes about github:
# To make a command line argument M-!
# First create the repo then clone with "git clone <url>
# When committing, make sure the use "double quotes"
# I think I only made pushing work from the github GUI?
# To complile from withing emacs, M-! python <file name> RET


import subprocess
import os
import time

thisFile = os.path.basename(__file__)

hashID = subprocess.check_output(["git", "describe", "--always"])
print(hashID.strip())

diffStr = subprocess.check_output(["git", "diff", "HEAD"])
# if there is a difference between the current file and "HEAD", it will
# have this line
diffLine = "diff --git a/" + thisFile + " b/" + thisFile
# .find() returns 0 if found, -1 if not found
isDiff = diffStr.find(diffLine) + 1
if isDiff:
    # update git and grab new hash
    print("Pushing changes to git...")
    subprocess.check_output(["git", "add", thisFile])
    timestr = time.strftime("%Y-%m-%d %H:%M:%S")
    subprocess.check_output(["git", "commit", "-m", timestr])

# Random line changed
# The first time this was pushed it had the id 3ca5939
# The second time it had the id c70ef16
