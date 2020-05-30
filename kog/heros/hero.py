# -*- coding: utf-8 -*-

import os
import re
import requests
from bs4 import BeautifulSoup

import sys

#reload(sys)
#sys.setdefaultencoding('utf-8')

baseurl = 'http://pvp.qq.com/web201605'
mainurl = 'http://pvp.qq.com/web201605/herolist.shtml'
herolist = []


def getHeroList():
    '''取所以英雄存入list中'''
    hero = {}
    res = requests.get(mainurl)
    sp = BeautifulSoup(res.content, "html.parser")
    lists = sp.select('body > div.wrapper > div > div > div.herolist-box > div.herolist-content > ul > li')
    for li in lists:
        oj = li.select('a')[0];
        hero['url'] = oj['href']
        hero['name'] = oj.text
        # 正则表达式取ename编号
        ename = re.findall('herodetail/(\d+)\.shtml', oj['href'])[0]
        hero['ename'] = ename
        herolist.append(hero)
        hero = {}
    return herolist


def saveImg(filepath, imgUrl):
    '''下载图片并保存'''
    r = requests.get(imgUrl, stream=True)
    with open(filepath, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()


if __name__ == '__main__':
    hlist = getHeroList()
    for hero in herolist:
        herodir = os.path.join(os.getcwd(), hero['name'])
        heropage = baseurl + '/' + hero['url']
        print('[%s]' % (herodir))
        res = requests.get(heropage)
        sop = BeautifulSoup(res.content, "html.parser")
        li = sop.select('body > div.wrapper > div.zk-con1.zk-con > div > div > div.pic-pf > ul ')[0]['data-imgname']
        li = str(li).split('|')
        print(li)
        # 遍历所有皮肤
        for i in range(len(li)):
            imgurl = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' \
                     + hero['ename'] + '/' + hero['ename'] + '-bigskin-' + str(i + 1) + '.jpg'
            imgname = os.path.join(herodir, li[i] + ".jpg")
            print('----[%s]--[%s]---' % (imgname, imgurl))
            # 创建英雄目录
            if os.path.exists(herodir) == False:
                os.mkdir(herodir)
            saveImg(imgname, imgurl)