import os
import subprocess
import shutil

counter = 0
command_stub = "raw2dng "
for rawfile in os.listdir("."):
    if rawfile.endswith(".RAW"):
        cmd = command_stub + '"' + rawfile + '"'
        subprocess.call(cmd, shell=True)
        for dngfile in os.listdir("."):
            if dngfile.endswith('.dng'):
                directory = "./%s" % counter
                if not os.path.exists(directory):
                    os.makedirs(directory)
                dest = os.path.join(directory, dngfile)
                shutil.move(dngfile, dest)
        counter += 1
