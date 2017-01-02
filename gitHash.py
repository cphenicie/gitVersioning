# Minimal working example of code that grabs the git hash for a file
import subprocess
hashID = subprocess.check_output(["git", "describe"])
print(hashID)
