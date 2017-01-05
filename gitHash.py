# Example using the tlab_git module
##
# Other notes about github:
# To make a command line argument M-!
# First create the repo then clone with "git clone <url>
# When committing, make sure the use "double quotes"
# I think I only made pushing work from the github GUI?
# To complile from withing emacs, M-! python <file name> RET
#
# To restore previous versions in emacs, click on the Git:master button or
# C-x v ~

import os
import tlab_git

thisFile = os.path.basename(__file__)
thisFileDir = os.path.dirname(os.path.realpath(__file__))
print(thisFileDir)



tlab_git.cphenicieCred()
hashStr = tlab_git.getHash(gitDir=thisFileDir)
print(hashStr[0:7])
isDiff = tlab_git.checkDiff(thisFileDir, thisFile)
if isDiff:
    tlab_git.updateRepo(thisFileDir, thisFile)
