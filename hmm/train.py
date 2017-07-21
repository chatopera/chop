#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <stakeholder> All Rights Reserved
#
# Refers:
# http://www.52nlp.cn/itenyh%E7%89%88-%E7%94%A8hmm%E5%81%9A%E4%B8%AD%E6%96%87%E5%88%86%E8%AF%8D%E5%9B%9B%EF%BC%9Aa-pure-hmm-%E5%88%86%E8%AF%8D%E5%99%A8
# https://raw.githubusercontent.com/Samurais/chinese_nlp/master/segment/segment.py
# File: /Users/hain/ai/chop/data/train.py
# Author: Hai Liang Wang
# Date: 2017-07-21:22:33:04
#
#===============================================================================

"""
   Train Model for HMM Tokenizer
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-21:22:33:04"


import os
import sys
import json
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(curdir, os.path.pardir))

TRAIN_CORPUS=os.path.join(curdir, 'msr_training.utf8')
TRAIN_VOCAB=os.path.join(curdir, 'pku_training_words.utf8')

import chop.util as helper
from functools import reduce

def __load_observations(vocab_path = TRAIN_VOCAB):
    '''
    load vocabulary from disk
    '''
    observations = []
    with open(vocab_path, 'r') as f:
        [observations.append(x.strip()) if x.strip() else None for x in f.readlines()]
    return observations

def __concat_sbme(result, term):
    '''
    encode a term as SBME
    '''
    term_length = len(term)
    
    if term_length == 1:
        result.append('S')
        return result

    term_ll = term_length - 1
    for i in range(term_length):
        if i == 0: result.append('B')
        elif i == term_ll: result.append('E')
        else: result.append('M')

    return result

def __dump_hmm(states, observations, pi, A, B):
    '''
    dump hmm data into file
    '''
    with open(os.path.join(curdir, 'hmm.json'), 'w') as outfile:  
        data = json.dumps(dict({
            "states": states,
            "observations": observations,
            "pi": pi,
            "A": A,
            "B": B
        }), indent=4, ensure_ascii=False)
        outfile.write(data)

def train_hmm(corpus_path = TRAIN_CORPUS, vocab_path = TRAIN_VOCAB):
    '''
    Train HMM Parameters with corpus and vocab
    '''
    states = ['B', 'M', 'E', 'S']
    observations = __load_observations()
    pi = {'B': 0.5, 'M': .0, 'E': .0, 'S': 0.5} # start_probability
    # transition probability matrix
    A = {'B':{'B':0, 'E':0, 'M':0, 'S':0}, 'E':{'B':0, 'E':0, 'M':0, 'S':0}, 'M':{'B':0, 'E':0, 'M':0, 'S':0}, 'S':{'B':0, 'E':0, 'M':0, 'S':0}}
    # emission probability matrix
    B = {'B':{}, 'E':{}, 'M':{}, 'S':{}}

    with open(corpus_path, 'r') as fin:
        for line in fin.readlines():
            terms = line.strip().split()
            [ terms.remove(t) if helper.is_terminator(t) or \
                    (len(t) ==1 and helper.is_punct(t)) else None for t in terms]
            if not terms:
                continue
            encoder = reduce(__concat_sbme, terms, [])
            helper.DEBUG(''.join(terms))
            helper.DEBUG(encoder)
            
            text = ''.join(terms)
            assert len(text) == len(encoder), "text should be mapped to state with equal length."

            for x, y in zip(encoder, encoder[1:]): # use zip to get bi-grams
                # transition probability matrix
                A[x][y] += 1

            for state, observation in zip(encoder, text):
                if observation in B[state]:
                    B[state][observation] += 1
                else:
                    B[state][observation] = 1

    # transition probability matrixfor (k_i, v_i) in 
    for k_i, v_i in A.items():
        count = sum(v_i.values())
        for (k_j, v_j) in v_i.items():
            # transition probability matrix
            A[k_i][k_j] = v_j / count

    count = .0
    for (k_i, v_i) in B.items():
        for item in observations:
            '''
            not tuning for words out of dict
            '''
            if item in v_i.keys():
                B[k_i][item] += 1 # 添加1进行平滑
            else:
                B[k_i][item] = 1  # 针对没有出现的词，将其出现频次设置为1
            count += B[k_i][item]

    for (k_i, v_i) in B.items():
        for (k_j, v_j) in v_i.items():
            B[k_i][k_j] = v_j / count	    

    __dump_hmm(states, observations, pi, A, B)

def test():
    helper.DEBUG("test")
    train_hmm()
    # __dump_hmm("A", "中文", "c", "d", "e")

if __name__ == '__main__':
    test()
