#!/usr/bin/env python

"""
Copyright (c) August Yip (http://august.hk/)
"""

import configparser
import os


dir = os.path.dirname(__file__)
config_file = os.path.join(dir, '../../config.ini')
config = configparser.ConfigParser()
config.read(config_file)

if config['Default']['symbols'] != '' :
  config.symbols = ['"' + symbol.strip() + '"' for symbol in config['Default']['symbols'].split(',')]


