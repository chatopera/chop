#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <stakeholder> All Rights Reserved
#
#
# File: /Users/hain/ai/chop/test.py
# Author: Hai Liang Wang
# Date: 2017-07-20:10:29:58
#
#===============================================================================

"""
   TODO: Module comments at here
   
   
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-20:10:29:58"


import os
import sys
import unittest
import argparse
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(curdir, os.path.pardir, os.path.pardir))

from chop.mmseg import Tokenizer, Word, Vocabulary, Chunk
from chop.util import DEBUG, INFO, WARN, ERROR

global args

class ChopTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_chunk_n_word(self):
        w1 = Word("中文", 1)
        w2 = Word("分词技术", 1)
        c1= Chunk(w1, w2)
        assert c1.total_word_length==6, "total_word_length"
        assert c1.average_word_length==c1.average_word_length , "average_word_length"
        assert c1.standard_deviation==0.5773502691896257 , "standard_deviation"
        assert c1.word_frequency==2, "word_frequency"
        INFO("passed.")

    def test_vocab(self):
        v = Vocabulary(dict_path=os.path.join(curdir, 'dict.txt'))
        INFO(len(v.dict))
        INFO(v.get_word("中文").text)
        INFO(v.get_word("中文").freq)
        INFO(v.get_word("中文").length)

    def test_seg(self):
        self.T = Tokenizer(dict_path=os.path.join(curdir, 'dict.txt'))
        INFO(' '.join(self.T.cut("CNN报道Washington D.C.即将开始新一轮的单边制裁朝鲜计划")))
        INFO(' '.join(self.T.cut("研究生命来源")))
        INFO(' '.join(self.T.cut("我们中出了一个叛徒")))
        INFO(' '.join(self.T.cut("南京市长江大桥欢迎您")))
        INFO(' '.join(self.T.cut("请把手抬高一点儿")))
        INFO(' '.join(self.T.cut("长春市长春节致词。")))
        INFO(' '.join(self.T.cut("长春市长春药店。")))
        INFO(' '.join(self.T.cut("我的和服务必在明天做好。")))
        INFO(' '.join(self.T.cut("我发现有很多人喜欢他。")))
        INFO(' '.join(self.T.cut("我喜欢看电视剧大长今。")))
        INFO(' '.join(self.T.cut("半夜给拎起来陪看欧洲杯糊着两眼半晌没搞明白谁和谁踢。")))
        INFO(' '.join(self.T.cut("李智伟高高兴兴以及王晓薇出去玩，后来智伟和晓薇又单独去玩了。")))
        INFO(' '.join(self.T.cut("一次性交出去很多钱。 ")))
        INFO(' '.join(self.T.cut("这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。")))
        INFO(' '.join(self.T.cut("我不喜欢日本和服。")))
        INFO(' '.join(self.T.cut("雷猴回归人间。")))
        INFO(' '.join(self.T.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")))
        INFO(' '.join(self.T.cut("我需要廉租房")))
        INFO(' '.join(self.T.cut("永和服装饰品有限公司")))
        INFO(' '.join(self.T.cut("我爱北京天安门")))
        INFO(' '.join(self.T.cut("abc")))
        INFO(' '.join(self.T.cut("隐马尔可夫")))
        INFO(' '.join(self.T.cut("雷猴是个好网站")))
        INFO(' '.join(self.T.cut("“Microsoft”一词由“MICROcomputer（微型计算机）”和“SOFTware（软件）”两部分组成")))
        INFO(' '.join(self.T.cut("草泥马和欺实马是今年的流行词汇")))
        INFO(' '.join(self.T.cut("伊藤洋华堂总府店")))
        INFO(' '.join(self.T.cut("中国科学院计算技术研究所")))
        INFO(' '.join(self.T.cut("罗密欧与朱丽叶")))
        INFO(' '.join(self.T.cut("我购买了道具和服装")))
        INFO(' '.join(self.T.cut("PS: 我觉得开源有一个好处，就是能够敦促自己不断改进，避免敞帚自珍")))
        INFO(' '.join(self.T.cut("湖北省石首市")))
        INFO(' '.join(self.T.cut("总经理完成了这件事情")))
        INFO(' '.join(self.T.cut("电脑修好了")))
        INFO(' '.join(self.T.cut("做好了这件事情就一了百了了")))
        INFO(' '.join(self.T.cut("人们审美的观点是不同的")))
        INFO(' '.join(self.T.cut("我们买了一个美的空调")))
        INFO(' '.join(self.T.cut("线程初始化时我们要注意")))
        INFO(' '.join(self.T.cut("一个分子是由好多原子组织成的")))
        INFO(' '.join(self.T.cut("祝你马到功成")))
        INFO(' '.join(self.T.cut("他掉进了无底洞里")))
        INFO(' '.join(self.T.cut("中国的首都是北京")))
        INFO(' '.join(self.T.cut("孙君意")))
        INFO(' '.join(self.T.cut("外交部发言人马朝旭")))
        INFO(' '.join(self.T.cut("领导人会议和第四届东亚峰会")))
        INFO(' '.join(self.T.cut("在过去的这五年")))
        INFO(' '.join(self.T.cut("还需要很长的路要走")))
        INFO(' '.join(self.T.cut("60周年首都阅兵")))
        INFO(' '.join(self.T.cut("你好人们审美的观点是不同的")))
        INFO(' '.join(self.T.cut("买水果然后来世博园")))
        INFO(' '.join(self.T.cut("买水果然后去世博园")))
        INFO(' '.join(self.T.cut("但是后来我才知道你是对的")))
        INFO(' '.join(self.T.cut("存在即合理")))
        INFO(' '.join(self.T.cut("的的的的的在的的的的就以和和和")))
        INFO(' '.join(self.T.cut("I love你，不以为耻，反以为rong")))
        INFO(' '.join(self.T.cut("hello你好人们审美的观点是不同的")))
        INFO(' '.join(self.T.cut("很好但主要是基于网页形式")))
        INFO(' '.join(self.T.cut("hello你好人们审美的观点是不同的")))
        INFO(' '.join(self.T.cut("为什么我不能拥有想要的生活")))
        INFO(' '.join(self.T.cut("后来我才")))
        INFO(' '.join(self.T.cut("此次来中国是为了")))
        INFO(' '.join(self.T.cut("使用了它就可以解决一些问题")))
        INFO(' '.join(self.T.cut(",使用了它就可以解决一些问题")))
        INFO(' '.join(self.T.cut("其实使用了它就可以解决一些问题")))
        INFO(' '.join(self.T.cut("好人使用了它就可以解决一些问题")))
        INFO(' '.join(self.T.cut("是因为和国家")))
        INFO(' '.join(self.T.cut("老年搜索还支持")))

    def test_punctuation(self):
        self.T = Tokenizer(dict_path=os.path.join(curdir, 'dict.txt'))
        INFO(' '.join(self.T.cut("2000年12月31日23时12分在北京妇产医院降生的宝宝赵辰蠧（右）和2001年1月1日零时9分23秒诞生的宝宝韩纪轮（左）在一起。（本报记者孟仁泉摄）", punctuation=True)))

    def test_basecase(self):
        global args
        self.T = Tokenizer(dict_path=os.path.join(curdir, 'dict.txt'))
        INFO(' '.join(self.T.cut(args.input, punctuation=True)))

if __name__ == '__main__':
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='长春市长春节致词。')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    # TODO: Go do something with args.input and args.filename

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main()
