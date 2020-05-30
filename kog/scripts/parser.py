#coding:utf-8
from scripts.conf import screen_dict
"""
    解析游戏界面数据：
        1、金币数目
        2、可释放技能、冷却时间、升级
        3、血量、蓝量
        4、敌人
        5、小地图（待定）
"""

class ParserConfig(object):

    def __init__(self):
        pass

    def get_small_map_coordinate(self):
        """
        获取小地图坐标
        :return:
        """
        return screen_dict['small_map_tap']

    def get_money_bag_coordinate(self):
        """
        获取钱袋坐标
        :return:
        """
        return screen_dict['money_bag']

    def get_recommend_equgeipment_coordinate_list(self):
        """
        获取推荐装备坐标
        :return:
        """
        return screen_dict['equipment_list']

    def get_roulette_coordinate(self):
        """
        获取施法轮盘坐标
        :return:
        """
        return screen_dict['roulette']

    def get_direction_coordinate(self, op=None):
        """
        获取方向坐标
        :param op: up、down、left、right
        :return:
        """
        if op == None:
            return (0, 0)
        return screen_dict['direction'][op]

    def get_attack_coordinate(self):
        """
        获取普通攻击键坐标
        :return:
        """
        return screen_dict['attack']

    def get_control__coordinate(self, type=None):
        """
        获取高级技能坐标
        :param type: 技能类型
        :return:
        """
        return screen_dict['control'][type]

    def get_the_back_coordinate(self):
        """
        获取回城功能坐标
        :return:
        """
        return screen_dict['control']['talent']['back']

    def get_the_treatment_coordinate(self):
        """
        获取治疗功能坐标
        :return:
        """
        return screen_dict['control']['talent']['treatment']

    def get_the_talent_coordinate(self):
        """
        获取天赋坐标
        :return:
        """
        return screen_dict['control']['talent']['talent']

    def get_skill_coordinate1(self):
        """
        获取一技能坐标
        :return:
        """
        return screen_dict['control']['skill']['skill_1']

    def get_skill_coordinate2(self):
        """
        获取二技能坐标
        :return:
        """
        return screen_dict['control']['skill']['skill_2']

    def get_skill_coordinate3(self):
        """
        获取三技能坐标
        :return:
        """
        return screen_dict['control']['skill']['skill_3']

    def get_up_coordinate1(self):
        """
        获取一技能升级坐标
        :return:
        """
        return screen_dict['control']['up']['up_1']

    def get_up_coordinate2(self):
        """
        获取二技能升级坐标
        :return:
        """
        return screen_dict['control']['up']['up_2']

    def get_up_coordinate3(self):
        """
        获取三技能升级坐标
        :return:
        """
        return screen_dict['control']['up']['up_3']

"""
from scripts.util import *

init()
print(device_x,device_y)

"""

