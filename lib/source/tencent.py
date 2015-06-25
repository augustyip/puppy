#!/usr/bin/env python3

import urllib.request
import urllib.parse

import json

from lib.core.data import config

class Tencent(object) :


  def quotes(self) :

    query_url = 'http://qt.gtimg.qq.com/?q=hkHSI,sh000001,r_hk00001,r_hk00005'
    request = urllib.request.Request(query_url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0')

    try :
      quote_results = []
      response = urllib.request.urlopen(request, timeout = 10)
      rows = response.read().decode(encoding='gb2312').split("\n")
      for row in rows :
        record = row[row.find('="') + 2 : -2].split('~')
        print(record)

    except :
      return self.quotes()


tencent = Tencent()
