# https://office54.net/python/app/subprocess-explorer-folder

import subprocess
path = r"J:\PC5-Working\3D\MikuMikuDance_v932x64\UserFile\Effect\ray-mmd-1.5.0\ray-mmd-1.5.0\Skybox"
path2 = r"E:\Dropbox\PC5_cloud\3D\HDRI"
path3 = r"E:\Dropbox\\PC5_cloud\\3D\\HDRI, J:\\PC5-Working\\3D\\MikuMikuDance_v932x64\\UserFile\\Effect\\ray-mmd-1.5.0\\ray-mmd-1.5.0\Skybox"
path4 = r"J:\PC5-Working\3D\MikuMikuDance_v932x64\UserFile\Effect\ray-mmd-1.5.0\ray-mmd-1.5.0\Skybox"
paths = [
    r"J:\PC5-Working\3D\MikuMikuDance_v932x64\UserFile\Effect\ray-mmd-1.5.0\ray-mmd-1.5.0\Skybox",
    r"E:\Dropbox\PC5_cloud\3D\HDRI"
]
# subprocess.Popen(['explorer', path, path2], shell=True) # failed
# subprocess.Popen(['explorer', path4], shell=True)

for item in paths:
    subprocess.Popen(['explorer', item], shell=True)