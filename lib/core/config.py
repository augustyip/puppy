#!/usr/bin/env python3

"""
Copyright (c) August Yip (http://august.hk/)
"""

import configparser
import os

class Config(object) :

  def __init__(self):
    dir = os.path.dirname(__file__)
    conf = configparser.ConfigParser()
    conf.read(os.path.join(dir, '../../config.ini'))

    source = conf['Default']['source']

    if source == 'Yahoo' :
      default_symbos = [
        '^HSI',
      ]
    elif source == 'Tencent' :
      default_symbos = [
        'hkHSI',
        'sh000001',
        'usDJI',
      ]

    if conf[source]['symbols'] != '' :
      symbols = [symbol.strip() for symbol in conf[source]['symbols'].split(',')]

    self.symbols = default_symbos + symbols

    self.config = conf

config = Config()
