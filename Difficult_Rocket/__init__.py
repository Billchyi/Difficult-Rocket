#  -------------------------------
#  Difficult Rocket
#  Copyright © 2021 by shenjackyuanjie
#  All rights reserved
#  -------------------------------

"""
writen by shenjackyuanjie
mail:   3695888@qq.com
github: @shenjackyuanjie
gitee:  @shenjackyuanjie
"""

__version__ = '0.6.1'

playing = False

if playing:
    from .api import new_thread

    @new_thread('think')
    def think(some_thing_to_think):
        gotcha = 'think_result'
        return gotcha
