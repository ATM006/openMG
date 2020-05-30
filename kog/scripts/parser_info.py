#coding:utf-8
import cv2
import numpy as np
import operator
from scripts.util import *
from scipy import ndimage
#from scripts.parser import ParserConfig






class ParserInfo(object):
    """
    解析游戏画面各种信息
    """

    def __init__(self):
        #self.image =  pull_screenshot(resize=True, save_file=True)
        self.friendly_bloods = [0, 0, 0, 0 ,0]
        self.enemy_bloods = [0, 0, 0, 0, 0]
        self.img_template = cv2.imread('../img/img_template.png')
        self.img_mask = cv2.imread('../img/img_mask.png')
        self.img_gray = cv2.imread('../img/screen.png')
        self.scale_ratio = 1.0
        pass




    def get_blood_volume(self):
        """

        获取血量
        :return:
        """
        self.img_gray = cv2.imread('../img/screen.png')

        img_template = cv2.cvtColor(self.img_template, cv2.COLOR_BGR2GRAY)
        img_mask = cv2.cvtColor(self.img_mask, cv2.COLOR_BGR2GRAY)
        img_gray = cv2.cvtColor(self.img_gray, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('../img/img_gray.png', img_gray)
        self.test_img = img_gray

        img_template = cv2.resize(img_template, None, fx=self.scale_ratio, fy=self.scale_ratio, interpolation=cv2.INTER_LINEAR)
        img_mask = cv2.resize(img_mask, None, fx=self.scale_ratio, fy=self.scale_ratio, interpolation=cv2.INTER_LINEAR)

        print(img_template.shape)
        print(img_mask.shape)
        print(img_gray.shape)

        #img_result = cv2.matchTemplate(img_gray, img_template, cv2.TM_CCORR_NORMED, mask=img_mask)
        img_result = cv2.matchTemplate(img_gray, img_template, cv2.TM_CCORR_NORMED, mask=img_mask)

        '''
        cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('result', img_result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''

        filter_size = 10
        img_max = ndimage.maximum_filter(img_result, size=filter_size * 2)

        '''
        cv2.namedWindow('max', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('max', img_max)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''

        maximum_idx = np.argwhere(img_result == img_max)
        print(maximum_idx.shape)
        maximum_value_list = []
        for i, j in maximum_idx:
            maximum_value_list.append([i, j, img_max[i][j], 0])

        print(maximum_value_list)
        maximum_value_list.sort(key=operator.itemgetter(2), reverse=True)
        maximum_value_list_top20 = maximum_value_list[:20]
        print(maximum_value_list_top20)

        alpha = 0.5
        beta = 0.5
        for item in maximum_value_list_top20:
            x, y = item[0], item[1]
            real_score = self.get_local_max_score(img_max,
                                         max_x=x, max_y=y,
                                         shape_x=36, shape_y=163,
                                         alpha=alpha, beta=beta)
            item[3] = real_score
            #print(real_score)

        #print(maximum_value_list_top20)
        maximum_value_list_top20.sort(key=operator.itemgetter(3), reverse=True)
        #print("max score list:", maximum_value_list_top20)

        return maximum_value_list_top20

    def get_local_max_score(self, img_max, max_x, max_y, shape_x, shape_y, alpha=1, beta=0):
        """
        计算像素分值，此函数基于两个要素——局部极大像素值，与周围像素的对比度
        :param img_max
        :param max_x:
        :param max_y:
        :param shape_x:
        :param shape_y:
        :param alpha:
        :param beta:
        :param test_img
        :return:
        """
        base_x = max_x - (shape_x/2)
        base_y = max_y - (shape_y/2)
        end_x = max_x + (shape_x/2)
        end_y = max_y + (shape_y/2)
        v0 = img_max[max_x][max_y]

        total = 0
        for i in range(int(base_x), int(end_x)):
            if i < shape_x/2 or i > 1280 - shape_x/2 : continue
            for j in range(int(base_y), int(end_y)):
                if j < shape_y/2 or j > 720 - shape_y/2: break
                if max_x == i and max_y == j:
                    continue
                total += img_max[i][j]
        avg_score = total / (shape_x * shape_y)

        return alpha * img_max[max_x][max_y] + beta * avg_score


if __name__ == '__main__':
    p = ParserInfo()
    x = p.get_blood_volume()
