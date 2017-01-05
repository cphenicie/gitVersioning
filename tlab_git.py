''' Integrate Git versioning in Python

This module provides functions useful for using Git to record which
source code is used to produce output files.

Functions:
    getHash -- returns the hash for the HEAD of the a branch
    checkDiff -- see if the current file is different from branch HEAD
    updateRepo -- update Git repository so current file is HEAD 

TODO:
    * Consider making a git class so we don't need to constantly pass
    fileDir argument
    * Consider using the GitPython package
'''

import subprocess
import os
import time


def getHash(gitDir):
    ''' returns the hash for the HEAD of the branch at gitDir

    Args:
        gitDir (str):  Directory containing .git file. If you want to 
            pass the path of the file calling this function, import 
            the os module and use 
            os.path.dirname(os.path.realpath(__file__))

    Returns:
        str: The hash for the HEAD of the specified directory 
    '''

    # subprocess will execute command line functions.
    # rev-list has a list of the hashes of all revisions to a git
    # repository (specified by the "cwd" argument).
    # either -1 or HEAD selects only the most recent revision
    # (not sure about the other of -1 and HEAD)
    # Not sure about "./"
    hashStr = subprocess.check_output(
        ["git", "rev-list", "-1", "HEAD", "./"], cwd=gitDir).strip()
    return hashStr


def checkDiff(fileDir, fileName):
    ''' see if the current file is different from branch HEAD

    Args:
        fileDir (str): Directory containing file to be checked
        fileName (str): Name of the file to be checked

    Returns:
        int: 1 if the files are different, 0 otherwise
    '''

    os.chdir(fileDir)
    diffStr = subprocess.check_output(["git", "diff", "HEAD"])
    diffLine = "diff --git a/" + fileName + " b/" + fileName
    # If there is a difference between the version of the file
    # currently running and the file at HEAD of the Git repo,
    # this line will be included in the diff output
    isDiff = diffStr.find(diffLine) + 1
    # .find() outputs -1 if not found, 0 if found.
    return isDiff


def updateRepo(fileDir, fileName):
    ''' update Git repository so current file is HEAD

    Args:
        fileDir (str): Directory containing file to be checked
        fileName (str): Name of the file to be checked


    Returns:
        str: hash of HEAD after committing

    '''
    print("Pushing changes to git...")
    os.chdir(fileDir)
    subprocess.check_output(["git", "add", fileName])
    timestr = time.strftime("%Y-%m-%d %H:%M:%S")
    subprocess.check_output(["git", "commit", "-m", timestr])
    newHash = subprocess.check_output(
        ["git", "rev-list", "-1", "HEAD", "./"], cwd=fileDir)
    print("The new hash is " + newHash)
    return newHash
