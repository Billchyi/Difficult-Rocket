#  -------------------------------
#  Difficult Rocket
#  Copyright © 2021-2022 by shenjackyuanjie 3695888@qq.com
#  All rights reserved
#  -------------------------------

"""
main.py
"""


class Error(Exception):
    """基础 Exception"""

    def __bool__(self):
        return False


class TexturesError(Error):
    """材质相关 error"""


class LanguageError(Error):
    """语言相关 error"""


class TestError(Error):
    """就像名字一样 用于测试的 error"""


"""
unsupport.py
"""


class NoMoreJson5(Error):
    """说什么我也不用Json5了！"""


class Nope418ImATeapot(Error):
    """我只是个茶壶而已，我不能煮咖啡！"""


class ThinkError(Error):
    """进不去，进不去，怎么想都进不去！"""


class BrainError(Error):
    """clever brain.png"""


class BigBrainError(BrainError):
    """bigbrain.png"""


class BrainTimeoutError(BrainError, ThinkError):
    """脑子····超时·······················啦！"""


"""
command.py
"""


class CommandError(Error):
    """命令解析相关 error"""


class CommandParseError(CommandError):
    """命令解析时出现错误"""


# QMark -> Quotation marks
# Pos -> Position

class CommandQMarkPosError(CommandParseError):
    """命令中,引号位置不正确
    例如： /command "aabcc "awdawd"""


class CommandQMarkMissing(CommandParseError):
    """命令中引号缺失
    例如: /command "aawwdawda awdaw """


class CommandQMarkConflict(CommandParseError):
    """命令中引号位置冲突
    例如: /command "aaaa "aaaa aaaa"""
    first_qmark_pos = None
    conflict_qmark_pos = None


class CommandQMarkPreMissing(CommandQMarkMissing):
    """命令中 前面的引号缺失
    例如: /command aaaa" aaaaaa"""
    suf_qmark_pos = None


class CommandQMarkSufMissing(CommandQMarkMissing):
    """命令中 后面的引号缺失(引号未闭合)
    例如: /command "aaaawaa some command"""
    pre_qmark_pos = None


"""
threading.py
"""


class LockTimeOutError(Error):
    """没有特殊指定的 ”某个“ 锁超时了"""
