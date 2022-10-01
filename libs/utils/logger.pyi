"""
:author shenjackyuanjie
:contact 3695888:qq.com
"""
#  -------------------------------
#  Difficult Rocket
#  Copyright © 2021-2022 by shenjackyuanjie 3695888@qq.com
#  All rights reserved
#  -------------------------------
import re
import os
import time
import enum
import atexit
import inspect
import threading

from logging import NOTSET, DEBUG, INFO, WARNING, ERROR, FATAL
from types import FrameType
from typing import Optional, Union, Dict, Iterable, Tuple, Any, List

os.system('')
# print(os.path.abspath(os.curdir))

# 如果想要直接使用 logger 来 logging
# 直接调用 logger.debug() 即可
# 默认配置会有
# ----------
# 配置方式一
# 直接使用 logger.Logger()
# 将会创建一个空 logger
# 可以自行通过
# 配置方式二


color_reset_suffix = "\033[0m"
""" 只是用来重置颜色的后缀 """

re_find_color_code = r'\033\[[^\f\n\r\t\vm]*m'
re_color_code = re.compile(re_find_color_code)

"""
OFF > FATAL > ERROR > WARN > INFO > FINE > FINER > DEBUG > TRACE > ALL
logging.py
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
"""
ALL = NOTSET
TRACE = 5
FINE = 7


class LoggingLevel(enum.IntEnum):
    """ 存储 logger 级别的 enum 类"""
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    FINE = 7
    TRACE = 5
    NOTSET = 0
    ALL = NOTSET


level_name_map = ...
name_level_map = ...
logger_configs = ...


class ThreadLock:
    """一个用来 with 的线程锁"""

    def __init__(self, the_lock: threading.Lock, time_out: Union[float, int] = 1 / 60) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...


class ListCache:
    """一个线程安全的列表缓存"""
    def __init__(self, lock: ThreadLock): ...
    def append(self, value: Union[str, Iterable[str]]): ...
    def __getitem__(self, item) -> str: ...
    def __call__(self, *args, **kwargs) -> List[str]: ...
    def __iter__(self): ...
    def __next__(self): ...
    def __bool__(self): ...
    @property
    def cache(self): ...
    def clear(self): ...


class LogFileCache:
    """日志文件缓存"""
    def __init__(self, file_conf: dict):
        """
        :param file_conf: 日志文件配置
        """
    def file_setup(self) -> None: ...
    def end_thread(self) -> None:
        """结束日志写入进程，顺手把目前的缓存写入"""
    def start_thread(self) -> None: ...
    @property
    def logfile_name(self) -> str: ...
    @logfile_name.setter
    def logfile_name(self, value: str) -> None: ...
    def _log_file_time_write(self, thread: bool = False) -> None: ...
    def write_logs(self, string: str, flush: bool = False) -> None: ...


class Logger:
    """shenjack logger"""
    def __init__(self,
                 name: str = 'root',
                 level: int = DEBUG,
                 file_conf: List[LogFileCache] = None,
                 colors: Dict[Union[int, str], Dict[str, str]] = None,
                 formats=None) -> None:
        """
        配置模式: 使用 kwargs 配置
        :param name: logger 名称 默认为 root
        :param level: logging 输出等级 默认为 DEBUG(10)
        :param file_conf: logger 的文件处理配置
        :param colors: dict 颜色配置
        :param formats: 格式化配置
        """
    def add_file(self, handler: LogFileCache) -> Nones: ...
    def remove_file(self, handler: LogFileCache) -> None: ...
    def make_log(self, *values: object,
                 level: int,
                 sep: Optional[str] = ' ',
                 end: Optional[str] = '\n',
                 flush: Optional[bool] = False,
                 frame: Optional[FrameType] = None) -> None: ...
    def format_text(self, level: int, text: str, frame: Optional[FrameType]) -> str: ...
    def trace(self, *values: object,
              sep: Optional[str] = ' ',
              end: Optional[str] = '\n',
              flush: Optional[bool] = False,
              frame: Optional[FrameType] = None) -> None: ...
    def fine(self, *values: object,
             sep: Optional[str] = ' ',
             end: Optional[str] = '\n',
             flush: Optional[bool] = False,
             frame: Optional[FrameType] = None) -> None: ...
    def debug(self,
              *values: object,
              sep: Optional[str] = ' ',
              end: Optional[str] = '\n',
              flush: Optional[bool] = False,
              frame: Optional[FrameType] = None) -> None: ...
    def info(self,
             *values: object,
             sep: Optional[str] = ' ',
             end: Optional[str] = '\n',
             flush: Optional[bool] = False,
             frame: Optional[FrameType] = None) -> None: ...
    def warning(self,
                *values: object,
                sep: Optional[str] = ' ',
                end: Optional[str] = '\n',
                flush: Optional[bool] = False,
                frame: Optional[FrameType] = None) -> None: ...
    def error(self,
              *values: object,
              sep: Optional[str] = ' ',
              end: Optional[str] = '\n',
              flush: Optional[bool] = False,
              frame: Optional[FrameType] = None) -> None: ...
    def fatal(self,
              *values: object,
              sep: Optional[str] = ' ',
              end: Optional[str] = '\n',
              flush: Optional[bool] = False,
              frame: Optional[FrameType] = None) -> None: ...


def get_key_from_dict(a_dict: Dict, key: Any, default: Any = None) -> Optional[Any]: ...
def format_str(text: str) -> str: ...
def len_without_color_maker(text: str) -> int: ...
def gen_file_conf(file_name: str,
                  file_level: int = DEBUG,
                  file_mode: str = 'a',
                  file_encoding: str = 'utf-8',
                  file_cache_len: int = 10,
                  file_cache_time: Union[int, float] = 1) -> dict:
    """
    生成一个文件配置
    :param file_name: 日志文件名
    :param file_level: 日志文件记录级别
    :param file_mode: 文件模式
    :param file_encoding: 文件编码
    :param file_cache_len: 文件缓存长度
    :param file_cache_time: 文件缓存时间
    :return: 生成的配置
    """
    return {'file_name':  file_name,
            'level':      file_level,
            'mode':       file_mode,
            'encoding':   file_encoding,
            'cache_len':  file_cache_len,
            'cache_time': file_cache_time}
def gen_color_conf(color_name: str = None, **colors) -> dict: ...
def logger_with_default_settings(name: str,
                                 level: int = DEBUG,
                                 file_conf: dict = None,
                                 colors: dict = None,
                                 formats: dict = None) -> Logger:
    return Logger(name=name,
                  level=level,
                  file_conf=[LogFileCache(gen_file_conf(**file_conf))],
                  colors=gen_color_conf(**colors),
                  formats=logger_configs['Formatter'].copy().update(formats))
def add_file_config(conf_name: str,
                    file_name: str,
                    file_level: int = DEBUG,
                    file_mode: str = 'a',
                    file_encoding: str = 'utf-8',
                    file_cache_len: int = 10,
                    file_cache_time: Union[int, float] = 1) -> None:
    """
    向 logger config 里添加一个文件配置
    :param conf_name: 文件配置名称
    :param file_name: 日志文件名
    :param file_level: 日志文件记录级别
    :param file_mode: 文件模式
    :param file_encoding: 文件编码
    :param file_cache_len: 文件缓存长度
    :param file_cache_time: 文件缓存时间
    :return: None
    """
    logger_configs['File'][conf_name] = {'file_name':  file_name,
                                         'level':      file_level,
                                         'mode':       file_mode,
                                         'encoding':   file_encoding,
                                         'cache_len':  file_cache_len,
                                         'cache_time': file_cache_time}
def get_logger(name: str = 'root') -> Logger:
    """
    此函数用于从 global_config 中取出对应的配置建立一个相应的 logger
    :param name: logger的名称 默认为 root
    :return: 创建好的 logger
    """
def test_logger(the_logger: Logger) -> None: ...
