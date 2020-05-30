#coding:utf-8
import os,sys
from scripts.util import *
from scripts.parser import ParserConfig

par = ParserConfig()

class Kog(object):

    def __init__(self):
        self.device_x ,self.device_y = find_screen_size()
        print(device_x)
        pass

    def check_small_map(self):
        """
        查看小地图
        :return:
        """
        tap_x, tap_y = par.get_small_map_coordinate()
        tap_screen(tap_x, tap_y)

    def parse_small_map(self):
        """
        解析小地图信息
        :return:
        """
        pass

    def get_money_bag(self):
        """
        获取金币数量
        :return: 金币数
        """
        pass

    def equipment_store(self, index=0):
        """
        打开装备商店，购买装备
        :return:
        """
        tap_x, tap_y = par.get_recommend_equgeipment_coordinate_list()[index]
        tap_screen(tap_x, tap_y)

    def control_roulette(self, op=None):
        """
        控制施法轮盘
        :param x:
        :param y:
        :return:
        """
        if op == None:
            return
        x, y = par.get_roulette_coordinate()
        x1, y1 = par.get_direction_coordinate(op)
        swipe(x, y, x1, y1, 1000)

    def attack(self):
        """
        普通攻击
        :return:
        """
        tap_x, tap_y = par.get_attack_coordinate()
        tap_screen(tap_x, tap_y)

    def get_skill_status(self):
        """
        获取技能状态：
        :return:
        """
        pass

    def smart_skill(self):
        """
        智能施法
        :return:
        """
        pass

    def advanced_control(self, type=None):
        """
        高级技能控制：默认普通攻击，或者执行指定类型技能
        :param type: 技能类型
        :return:
        """
        tap_x, tap_y = par.get_control__coordinate(type)
        tap_screen(tap_x, tap_y)

