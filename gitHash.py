# Minimal working example of code that grabs the git hash for a file
#
# Other notes about github:
# To make a command line argument M-!
# First create the repo then clone with "git clone <url>
# When committing, make sure the use "double quotes"
# I think I only made pushing work from the github GUI?
# To complile from withing emacs, M-! python <file name> RET


import subprocess
import os

thisFile = os.path.basename(__file__)

hashID = subprocess.check_output(["git", "describe", "--always"])
print(hashID.strip())

diffStr = subprocess.check_output(["git", "diff", "HEAD"])
# if there is a difference between the current file and "HEAD", it will
# have this line
diffLine = "diff --git a/" + thisFile + " b/" + thisFile

# The first time this was pushed it had the id 3ca5939
# The second time it had the id c70ef16
