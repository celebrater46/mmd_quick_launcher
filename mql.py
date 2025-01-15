# https://office54.net/python/app/subprocess-explorer-folder

import subprocess

paths = [
    r"J:\PC5-Working\3D\MikuMikuDance_v932x64\UserFile\Project",
    r"E:\Dropbox\PC5_cloud\3D\HDRI",
    r"J:\PC5-Working\3D\MikuMikuDance_v932x64\UserFile\Effect\ray-mmd-1.5.0\ray-mmd-1.5.0",
    r"J:\PC5-Working\3D\MikuMikuDance_v932x64\UserFile"
]

for item in paths:
    subprocess.Popen(['explorer', item], shell=True)