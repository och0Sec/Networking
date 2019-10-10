#!/usr/bin/env python3

#Import Modules needed to run our functions successfully
import zipfile, os
from datetime import date, timedelta

#Get yesterday's date.
yesterday = date.today() - timedelta(days=1)
ydate = yesterday.strftime('%Y-%m-%d')

#Specify the path to where our zip file will be saved. 
path = '/backups'
fullpath = os.path.join(path,ydate)
file = zipfile.ZipFile(fullpath + '.zip','w')

#Change the working directory to where the files to be compressed are.
os.chdir('/backups')

#Nested If statement in case there are files that match our criteria
#and delete original file after compressing.
for x in os.listdir():
    if x.startswith(ydate) and x.endswith('.config'):
        file.write(x, compress_type = zipfile.ZIP_DEFLATED)
        os.remove(x)
file.close()

