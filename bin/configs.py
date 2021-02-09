"""
writen by shenjackyuanjie
mail: 3695888@qq.com
"""

# import re
import os
import time
import json5
import decimal
import logging

try:
    import tools
except ModuleNotFoundError:
    from bin import tools

# logger
configs_logger = logging.getLogger('configs')


def _BasicNumber(int_num=0, float_num=1, unit1=None, unit2=None) -> list:
    if unit1 is None:
        unit1 = []
    if unit2 is None:
        unit2 = []
    if tools.is_decimal(float_num):  # is decimal class?
        return [int_num, float_num, unit1, unit2]  # is just return
    else:
        return [int_num, decimal.Decimal(str(float_num)), unit1, unit2]  # no create a decimal class


def BasicNumber(int_num=0, float_num=1, unit1=None, unit2=None, num=1) -> list:
    numbers = []
    if num > 1:
        for x in range(0, num, 1):
            numbers.append(_BasicNumber(int_num, float_num, unit1, unit2))
    elif num == 1:
        return _BasicNumber(int_num, float_num, unit1, unit2)
    else:  # num < 1
        raise TypeError('you should give me a num with >= 1!')
    return numbers


class BasicNumberClass:
    def __init__(self, int_num=0, float_num=1, unit1=None, unit2=None):
        self.int = int_num
        self.float = decimal.Decimal(str(float_num))
        if unit1:
            self.units1 = unit1
        else:
            self.units1 = []
        if unit2:
            self.units2 = unit2
        else:
            self.units2 = []

    def sort(self):
        self.units1.sort()
        self.units2.sort()

    def units(self):
        return [].append(self.units1.append(self.units2))

    def __str__(self):
        return None

    def __add__(self, other):
        if type(other) is type(self):
            self.sort()
            other.sort()
            if self.units() == other.units():
                pass

    def __radd__(self, other):
        self.__add__(self)

    def __mul__(self, other):
        pass


def basic_poi(poi_type=None) -> list:
    if poi_type is None:
        return BasicNumber(unit1='m', num=2)
    if poi_type == 'chunk':
        return [BasicNumber(unit1='chunk', num=2), BasicNumber(unit1='m', num=2)]


def basic_force() -> list:
    return BasicNumber(unit1='N', num=2)


def configs(name, option=None) -> dict:
    with open(name, 'r') as file:
        data = json5.load(file)
        if option:
            try:
                data = data[option]
            except IndexError as exp:
                log = 'can\'t find stack named %s in file %s' % (option, name)
                configs_logger.exception(log)
                raise IndexError(log)
        return data


def name_handler(name: str, configs=None) -> str:
    if configs is None:
        return name
    for need_replace in configs:
        replace = configs[need_replace]
        if need_replace == '{date}':  # special replaces
            replace = time.strftime(configs[need_replace], time.gmtime(time.time()))
        elif need_replace == '{time.time}':
            replace = time.time()
        elif need_replace == '{dir}':
            replace = os.getcwd()
        name.replace(need_replace, replace)
