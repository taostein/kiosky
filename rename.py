
# Copy or move the files into a normal name
import re
import os
files = os.listdir() 
regex = '\\[([A-Za-z0-9_\\-]+)\\]\\.webm$'
# regex = re.escape('[([A-Za-z0-9_-]+)].webm$')
for file in files:
    match = re.search(regex, file)
    if match != None:
        key = match.group(1)
        file = file.replace("'", re.escape("'\"'\"'"))
        cmd = "cp '" + file + "' " + key + ".webm"
        print(cmd)

