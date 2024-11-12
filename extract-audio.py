
import re
import os
files = os.listdir()
regex = '^([A-Za-z0-9_\\-]{11}).(webm|mp4)$'
for file in files:
    match = re.match(regex, file)
    if match != None:
        key = match.group(1)
        print("ffmpeg -i " + file + " " + key + ".mp3")

