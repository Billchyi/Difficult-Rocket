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

from libs import pyglet
from libs.pyglet.gui import widgets
from libs.pyglet.sprite import Sprite
from libs.pyglet.graphics import Batch
from libs.pyglet.image import AbstractImage


class Parts(widgets.WidgetBase):
    """
    parts
    """
    def __init__(self,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 textures: AbstractImage,
                 batch: Batch,
                 parts_data: dict):
        super().__init__(x, y, width, height)
        self.sprite = Sprite(img=textures, x=x, y=y, batch=batch)
        self._value = 0
