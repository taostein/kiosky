
# Copy or move the files into a normal name
import re
import os
files = os.listdir() 
regex = '\\[([A-Za-z0-9_\\-]{11})\\]\\.(webm|mp4)$'
for file in files:
    match = re.search(regex, file)
    if match != None:
        key = match.group(1)
        suffix = match.group(2)
        file = file.replace("'", re.escape("'\"'\"'"))
        cmd = "cp '" + file + "' " + key + "." + suffix
        print(cmd)

