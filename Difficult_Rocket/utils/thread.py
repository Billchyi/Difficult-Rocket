#  -------------------------------
#  Difficult Rocket
#  Copyright © 2021-2022 by shenjackyuanjie 3695888@qq.com
#  All rights reserved
#  -------------------------------

"""
writen by shenjackyuanjie
mail:   3695888@qq.com
github: @shenjackyuanjie
gitee:  @shenjackyuanjie
"""

import threading

from Difficult_Rocket import crash


class Threads(threading.Thread):
    def run(self):
        if crash.record_thread:
            crash.all_thread.append(self)
        super().run()
