#coding:utf-8

import time
from scripts.util import *
from scripts.conf import *
from scripts.kog import Kog

test = screen_dict['attack']
kog = Kog()

#time.sleep(5)
#print('small_map')
#kog.check_small_map()
#time.sleep(5)
#print('store')
#kog.equipment_store()

while True:
    time.sleep(1)


    kog.equipment_store(index=0)

    kog.control_roulette(op='down')



    kog.attack()
    kog.attack()
    kog.attack()
    kog.attack()
    kog.attack()
    kog.control_roulette(op='right')
    kog.advanced_control(type='up_1')
    kog.advanced_control(type='skill_1')
    kog.attack()
    kog.attack()
    kog.attack()
    kog.attack()
    kog.control_roulette(op='up')
    kog.advanced_control(type='up_2')
    kog.advanced_control(type='skill_2')
    kog.attack()
    kog.attack()
    kog.attack()
    kog.control_roulette(op='left')
    kog.advanced_control(type='up_3')
    kog.advanced_control(type='skill_3')
    kog.attack()
    kog.attack()
    kog.attack()
    kog.attack()



    print('hhhhh')