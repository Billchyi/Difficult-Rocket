'''
writen by shenjackyuanjie
mail: 3695888@qq.com
'''

import multiprocessing as mp

import pyglet
import pyglet.app
from pyglet import image
from pyglet.window import Window

try:
    # been import use
    from bin import configs
    from bin import tools
except (ModuleNotFoundError, ImportError, ImportWarning):
    # editing use
    import configs
    import tools


class client(mp.Process):
    def __init__(self, logger, dev_dic=None, dev_list=None, net_mode='local'):
        mp.Process.__init__(self)
        # logging
        self.logger = logger
        # share memory
        self.dev_list = dev_list
        self.dev_dic = dev_dic
        # value
        self.process_id = 'Client'
        self.process_name = 'Client process'
        self.view = 'space'
        self.net_mode = net_mode
        self.window_config = tools.config('sys_value/window.json5')
        self.window = window(logger=logger,
                             dev_dic=dev_dic,
                             dev_list=dev_list,
                             net_mode=net_mode,
                             width=int(self.window_config['width']),
                             height=int(self.window_config['height']),
                             fullscreen=tools.c_b(self.window_config['full_screen']),
                             caption=str(self.window_config['caption']),
                             visible=tools.c_b(self.window_config['visible']))

    def start(self) -> None:
        pyglet.app.run()


class window(pyglet.window.Window):

    def __init__(self, logger, dev_dic=None, dev_list=None, net_mode='local', *args, **kwargs):
        super(window, self).__init__(*args, **kwargs)
        """
        :param dev_list: 共享内存
        :param dev_dic: 共享内存
        :param logger: logger
        :param net_mode: 网络模式 # local / ip
        """
        # logging
        self.logger = logger
        # share memory
        self.dev_list = dev_list
        self.dev_dic = dev_dic
        # value
        self.process_id = 'Client'
        self.process_name = 'Client process'
        self.view = 'space'
        self.net_mode = net_mode
        # configs
        self.view = tools.config('configs/view.json5')
        self.map_view = [configs.basic_poi(poi_type='chunk')]
        self.part_list = tools.config('sys_value/parts.json5')
        # dic
        self.ships = {}  # all ship(part)
        self.planet_system = tools.config('sys_value/planet.json5')
        # hole planet system
        # list
        # re stuff
        # window
        self.logger.info('client setup done!')
        self.textures = {}
        # setup
        self.setup()

    def setup(self):
        # net_mode
        if self.net_mode == 'local':
            pass
        # parts
        self.textures['part'] = {}
        parts = tools.config('sys_value/parts.json5')
        for part in parts:
            path = parts[part][2][0]
            path = 'textures/' + path
            part_image = image.load(path)
            self.textures['part'][part] = part_image

    # draws

    def on_draw(self):
        return

    def build_draw(self):
        pass

    def space_draw(self):
        # render parts
        for ship in self.ships:
            # get ship poi
            ship_poi = ship['brain'][3]
            distances = tools.distance(ship_poi, self.map_view)
            for part in ship:
                pass

    def draw_label(self):
        pass

    """
    keyboard and mouse input
    """

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass
