# Minimal working example of code that grabs the git hash for a file
#
# Other notes about github:
# To make a command line argument M-!
# First create the repo then clone with "git clone <url>
# When committing, make sure the use "double quotes"
# I think I only made pushing work from the github GUI?
# To complile from withing emacs, M-! python <file name> RET


import subprocess
hashID = subprocess.check_output(["git", "describe", "--always"])
print(hashID.strip())
