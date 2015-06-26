#!/usr/bin/env python3

"""
Copyright (c) August Yip (http://august.hk/)
"""

import configparser
import os


dir = os.path.dirname(__file__)
config_file = os.path.join(dir, '../../config.ini')
config = configparser.ConfigParser()
config.read(config_file)

config.source = config['Default']['source']

if config.source == 'yahoo' :
  default_symbos = [
    '^HSI',
  ]

  if config['Yahoo']['symbols'] != '' :
    config.symbols = [symbol.strip() for symbol in config['Yahoo']['symbols'].split(',')]

elif config.source == 'tencent' :

  default_symbos = [
    'hkHSI',
    'sh000001',
    'usDJI',
  ]

  if config['Tencent']['symbols'] != '' :
    config.symbols = [symbol.strip() for symbol in config['Tencent']['symbols'].split(',')]


config.symbols = default_symbos + config.symbols


