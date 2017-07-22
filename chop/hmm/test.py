#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <stakeholder> All Rights Reserved
#
#
# File: /Users/hain/ai/chop/chop/hmm/test.py
# Author: Hai Liang Wang
# Date: 2017-07-22:16:27:53
#
#===============================================================================

"""
   TODO: Module comments at here
   
   
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-22:16:27:53"


import os
import sys
import unittest
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(curdir, os.path.pardir, os.path.pardir))

from chop.hmm import Tokenizer
import chop.util as helper

class HMMSegTest(unittest.TestCase):

    def setUp(self):
        self.T = Tokenizer()

    def test_punctuation(self):
        helper.DEBUG(' '.join(self.T.cut('作为市长，我也体会到这种危险。', punctuation = False)))

    def test_seg(self):
        helper.DEBUG(' '.join(self.T.cut('＊  ＊  ＊  ＊  ＊')))

    def test_oov(self):
        helper.DEBUG(' '.join(self.T.cut('温济泽')))
        
        helper.DEBUG(' '.join(self.T.cut('桑新')))

if __name__ == '__main__':
    unittest.main()
