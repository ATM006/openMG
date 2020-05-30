#coding:utf-8
import os,sys
import time
import logging
from PIL import Image

baseline = {}

SCREEN_PATH = '../img/screen.png'

# 屏幕分辨率
device_x, device_y = 1280, 720
base_x, base_y = 1280, 720



def init():
    find_screen_size()


def convert_cord(x,y):
    real_x = int(x / base_x * device_x)
    real_y = int(y / base_y * device_y)
    return real_x, real_y


def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    #real_x, real_y = convert_cord(x, y)
    real_x = x
    real_y = y
    #print('input tap {} {}'.format(real_x, real_y))
    os.system('adb shell input tap {} {}'.format(real_x, real_y))


def stop_game():
    os.system('am force-stop com.tencent.tmgp.sgame')  # 关闭游戏


def start_game():
    os.system('monkey -p com.tencent.tmgp.sgame -c android.intent.category.LAUNCHER 1')  # 打开游戏

    time.sleep(60)

    tap_screen(643, 553)

    logging.info("等待1分钟")

    time.sleep(60)

    logging.info("关闭广告")
    for i in range(5):  # 关闭广告
        tap_screen(1174, 77)


def restart_game():
    stop_game()

    logging.info("休息10分钟")
    time.sleep(60 * 10)

    logging.info("重启游戏")

    start_game()


def tap_center(top_left, bottom_right):
    tap_screen((top_left[0] + bottom_right[0])/2, (top_left[1] + bottom_right[1])/2)

"""
def tap_by_name(name):
    top_left = tap_cords[name][:2]
    bottom_right = tap_cords[name][2:]
    tap_center(top_left, bottom_right)
"""

def swipe(x, y, x1, y1, duration):
    print('adb shell input swipe {} {} {} {} {}'.format(x, y, x1, y1, duration))
    os.system('adb shell input swipe {} {} {} {} {}'.format(x, y, x1, y1, duration))


def find_screen_size():
    global device_x
    global device_y
    img = pull_screenshot(False)
    device_x, device_y = img.size
    logging.info('device size x, y = ({}, {})'.format(device_x, device_y))
    return device_x, device_y

"""
def save_crop():
    for key, val in tap_cords.items():
        img = Image.open('img/' + key + '.png')
        img.crop(val).save('img/crop_'+key+'.png')
"""


def pull_screenshot(resize=False, save_file=False):
    if save_file and os.path.exists(SCREEN_PATH):
        os.remove(SCREEN_PATH)

    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png {}'.format(SCREEN_PATH))
    img = Image.open(SCREEN_PATH)

    if resize and img.size != (base_x, base_y):
        return img.resize((base_x, base_y))
    else:
        return img


"""
def check_action():
    if not baseline:
        for n in ACTIONS:
            baseline[n] = np.array(Image.open('img/crop_' + n + '.png'))

    frame = pull_screenshot()

    crop_frame = {}
    for key, val in tap_cords.items():
        crop_frame[key] = np.sum(baseline[key] - np.array(frame.crop(val))) / baseline[key].size

    min_key = min(crop_frame, key=crop_frame.get)
    if crop_frame[min_key] < threshold:
        logging.debug("ACTION: {}".format(min_key))
        return min_key

    logging.debug("ACTION: no action")

    return None


def check_single_action(name):
    if not baseline:
        for n in ACTIONS:
            baseline[n] = np.array(Image.open('img/crop_' + n + '.png'))

    frame = pull_screenshot()

    res = np.sum(baseline[name] - np.array(frame.crop(tap_cords[name]))) / baseline[name].size

    if res < threshold:
        return True

    return False


def generate_hero_img():
    frame = pull_screenshot(save_file=True)
    y = 72
    h = 138
    x = 10
    w = 120
    row_num = 9
    col_num = 4

    base = 0

    if not os.path.exists('hero'):
        os.mkdir('hero')

    for j in range(col_num):
        for i in range(row_num):
            x_start = x + i * w
            y_start = y + j * h
            y_end = y_start + 100
            x_end = x_start + 100
            frame.crop((x_start, y_start, x_end, y_end)).save("hero/{}.png".format(j * row_num + i + base))

"""
