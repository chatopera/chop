

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <stakeholder> All Rights Reserved
#
#
# File: wordseg-algorithm/mmseg_example.py
# Author: Hai Liang Wang
# Date: 2017-07-19:22:25:38
#
#===============================================================================

"""
    MMSEG: 
    A Word Identification System for Mandarin Chinese Text Based on Two
    Variants of the Maximum Matching Algorithm
    http://technology.chtsai.org/mmseg/

    Other references:
    http://blog.csdn.net/nciaebupt/article/details/8114460
    http://www.codes51.com/itwd/1802849.html

    Dict:
    https://github.com/Samurais/jieba/blob/master/jieba/dict.txt

    Deps:
    Python3
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-19:22:25:38"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

import math
import string
from functools import reduce 

class Word():
    '''
    A single word
    '''
    def __init__(self, text="", freq=0):
        self.text = text
        self.freq = freq
        self.length = len(text)

class Chunk():
    '''
    Word Group that split with Forward Maximum Match(FMM)
    '''

    def __init__(self, w1, w2 = None, w3 = None):
        self.words = []
        self.words.append(w1)
        if w2: self.words.append(w2)
        if w3: self.words.append(w3)

    @property
    def total_word_length(self):
        return reduce(lambda x, y: x + y.length, self.words, 0)

    @property
    def average_word_length(self):
        return float(self.total_word_length) / float(len(self.words))

    @property
    def standard_deviation(self):
        return math.sqrt(reduce(lambda x,y: x + \
                        (y.length - self.average_word_length)**2, \
                        self.words, 0.0) / self.total_word_length)
    @property
    def word_frequency(self):
        return reduce(lambda x, y: x + y.freq, self.words, 0)


class Vocabulary():
    '''
    Vocabulary with whole words
    '''

    def __init__(self, dict_path):
        self.dict = {}
        self.dict_path = dict_path
        self.max_word_length = 0
        self.__load()
        

    def __load(self):
        with open(self.dict_path) as f:
            for x in f.readlines():
                if not x.startswith("#"):
                    text, freq, tag = x.split()
                    self.dict[text] = (len(text), int(freq), tag)
                    self.max_word_length = max([self.max_word_length, len(text)])

    def get_word(self, text):
        if text in self.dict: 
            return Word(text=text, freq=self.dict[text][1])


class Tokenizer():
    '''
    MMSEG Tokenizer for Python
    '''
    def __init__(self, dict_path):
        print('Vocabulary loaded.')
        self.V = Vocabulary(dict_path=dict_path)
        

    def cut(self, sentence):
        sentence_length = len(sentence)
        cursor = 0

        while cursor < sentence_length:
            if self.is_chinese_char(sentence[cursor]):
                print('__get_chunks')
                chunks = self.__get_chunks(sentence, cursor) # Matching Algorithm
                words, length = self.__ambiguity_resolution(chunks) # Ambiguity Resolution Rules
                cursor += length
                for term in list(filter(None, words)): yield term
            else: # 处理非中文单词(英文单词, etc.)
                word, cursor = self.__match_none_chinese_words(sentence, cursor)
                yield word

    def __ambiguity_resolution(self, chunks):
        '''
        根据当前游标位置进行切词
        '''
        print("# Rule 1: 根据 total_word_length 进行消岐")
        for x in chunks: [print(y.text) for y in x.words]; print('-'*20)
        if len(chunks) > 1: # Rule 1: 根据 total_word_length 进行消岐
            score = max([x.total_word_length for x in chunks])
            chunks = list(filter(None, \
                            [ x if x.total_word_length == score \
                                else None for x in chunks]))

        print("# Rule 2: 根据 average_word_length 进行消岐") 
        # for x in chunks: [print(y.text) for y in x.words]; print('-'*20)
        if len(chunks) > 1: # Rule 2: 根据 average_word_length 进行消岐
            score = max([x.average_word_length for x in chunks])
            chunks = list(filter(None, \
                            [ x if x.average_word_length == score \
                                else None for x in chunks]))

        if len(chunks) > 1: # Rule 3: 根据 standard_deviation 进行消岐
            score = max([x.standard_deviation for x in chunks])
            chunks = list(filter(None, \
                            [ x if x.standard_deviation == score \
                                else None for x in chunks]))

        if len(chunks) > 1: # Rule 4: 根据 word_frequency 进行消岐
            score = max([x.word_frequency for x in chunks])
            chunks = list(filter(None, \
                            [ x if x.word_frequency == score \
                                else None for x in chunks]))

        if len(chunks) != 1: 
            '''
            分词失败
            '''
            return ''

        words = chunks[0].words
        return [w.text for w in words], reduce(lambda x,y: x + y.length, words ,0)

    def __get_chunks(self, sentence, cursor):
        '''
        根据游标位置取词组
        '''
        chunks = []
        
        chunk_begin = self.__match_chinese_words(sentence, cursor)
        for b in chunk_begin: 
            chunk_middle = self.__match_chinese_words(sentence, cursor + b.length)
            if chunk_middle:
                for m in chunk_middle:
                    chunk_end = self.__match_chinese_words(sentence, cursor + b.length + m.length)
                    if chunk_end:
                        for e in chunk_end: 
                            chunks.append(Chunk(b, m, e))
                    else:
                        chunks.append(Chunk(b, m))
            else:
                chunks.append(Chunk(b))

        return chunks

    @staticmethod
    def __match_none_chinese_words(sentence, begin_pos):
        '''
        切割出非中文词
        '''
        # Skip pre-word whitespaces and punctuations
        #跳过中英文标点和空格
        cursor = begin_pos
        while cursor < len(sentence):
            ch = sentence[cursor]
            if Tokenizer.is_ascii_char(ch) or Tokenizer.is_chinese_char(ch):
                break
            cursor += 1
        #得到英文单词的起始位置    
        start = cursor
        
        #找出英文单词的结束位置
        while cursor < len(sentence):
            ch = sentence[cursor]
            if not Tokenizer.is_ascii_char(ch):
                break
            cursor += 1
        end = cursor
        
        #Skip chinese word whitespaces and punctuations
        #跳过中英文标点和空格
        while cursor < len(sentence):
            ch = sentence[cursor]
            if Tokenizer.is_ascii_char(ch) or Tokenizer.is_chinese_char(ch):
                break
            cursor += 1
            
        #返回英文单词和游标地址
        return sentence[start:end], cursor

    def __match_chinese_words(self, sentence, begin_pos):
        '''
        根据游标位置取词
        '''
        sentence_length = len(sentence)
        words = []
        cursor = begin_pos
        index = 0

        while cursor < sentence_length:
            if index >= self.V.max_word_length: break
            if not self.is_chinese_char(sentence[cursor]): break

            cursor += 1
            index += 1
            text = sentence[begin_pos:cursor]
            word = self.V.get_word(text)
            if word: words.append(word)

        if not words: 
            word = Word()
            word.length = 0
            words.append(word)

        return words

    @staticmethod
    def is_ascii_char(charater):
        if charater in string.whitespace:
            return False
        if charater in string.punctuation:
            return False
        return charater in string.printable

    @staticmethod 
    def is_chinese_char(charater):
        '''
        判断该字符是否是中文字符（不包括中文标点）
        '''  
        return 0x4e00 <= ord(charater) < 0x9fa6

if __name__ == '__main__':
    pass
