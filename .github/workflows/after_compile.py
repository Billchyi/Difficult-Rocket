#  -------------------------------
#  Difficult Rocket
#  Copyright © 2021-2022 by shenjackyuanjie 3695888@qq.com
#  All rights reserved
#  -------------------------------

import os
import sys
import zipfile

if sys.platform == "win32":
    os.system('')

print(os.listdir('./build'))

with zipfile.ZipFile('./build/main.zip', 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as dist_zip:
    for path, sub_paths, sub_files in os.walk('./build/Difficult-Rocket'):
        print(f'writing {path}')
        for file in sub_files:
            file_path = os.path.join(path, file)
            dist_zip.write(file_path)

