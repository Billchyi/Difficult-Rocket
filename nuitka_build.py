#  -------------------------------
#  Difficult Rocket
#  Copyright © 2020-2023 by shenjackyuanjie 3695888@qq.com
#  All rights reserved
#  -------------------------------

import sys
import time
import shutil
import zipfile
import subprocess

from pathlib import Path

from libs.utils import nuitka

if __name__ == '__main__':
    compiler = nuitka.CompilerHelper()

    # 修改 python 执行文件 为 运行时的 python
    compiler.python_cmd = sys.executable

    # 检测 --output xx 参数
    if '--output' in sys.argv:
        # 输入的是输出目录
        compiler.output_path = sys.argv[sys.argv.index('--output') + 1]
        sys.argv.remove('--output')
        sys.argv.remove(compiler.output_path)

    # 检测 --github 参数
    is_github = False
    if '--github' in sys.argv:
        is_github = True
        compiler.use_ccache = False
        compiler.show_progress = False
        compiler.output_path = Path('./build/github')

    print(compiler.output_path)

    print(compiler)

    print(compiler.gen_subprocess_cmd())

    # 确认是否需要编译
    # 如果包含 -y 参数 则直接编译
    if ('-y' or '-n') not in sys.argv or not is_github:
        while (do_compile := input('Do you want to compile this file? (y/n) ')) not in ['y', 'n']:
            pass
    elif '-y' in sys.argv:
        do_compile = 'y'
    elif is_github:
        do_compile = 'y'
    else:
        do_compile = 'n'

    if do_compile == 'y':
        # 编译
        start_time = time.time_ns()
        subprocess.run(compiler.gen_subprocess_cmd())
        print('Compile Done!')
        print(f'Compile Time: {time.time_ns() - start_time} ns ({(time.time_ns() - start_time) / 1000_000_000} s)')
        if is_github:
            subprocess.run(['python', 'libs/utils/github.py', compiler.output_path])
