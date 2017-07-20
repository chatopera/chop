#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
LVL = dict({
    "DEBUG": 10,
    "INFO": 20,
    "WARN": 30,
    "ERROR": 40
})

LOG_LVL = os.environ['CHOP_LOG_LVL'] if 'CHOP_LOG_LVL' in os.environ else "ERROR"

def INFO(s):
    print(LOG_LVL)
    if 20 >= LVL[LOG_LVL]:
        print(s)

def WARN(s):
    if 30 >= LVL[LOG_LVL]:
        print(s)

def DEBUG(s):
    if 10 >= LVL[LOG_LVL]:
        print(s)

def ERROR(s):
    if 40 >= LVL[LOG_LVL]:
        print(s)
    