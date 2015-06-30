#!/usr/bin/env python3

import urllib.request
import urllib.parse

import json

from lib.core.config import config

class Tencent(object) :


  def quotes(self) :

    query_url = 'http://qt.gtimg.qq.com/?q=' + ','.join(config.symbols)
    request = urllib.request.Request(query_url)
    request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0')

    try :
      response = urllib.request.urlopen(request, timeout = 10)
      rows = response.read().decode(encoding='gb2312').split("\n")
      quote_results = []
      for row in rows :
        if len(row) > 1 :
          result = {}
          record = row[row.find('="') + 2 : -2].split('~')
          result['Symbol'] = record[2]
          result['Name'] = record[46]
          result['LastTradePriceOnly'] = record[3]
          result['Change'] = record[31]
          result['ChangeinPercent'] = record[32] + '%'
          result['DaysLow'] = record[34]
          result['DaysHigh'] = record[33]
          quote_results.append(result)

      return quote_results
    except :
      return self.quotes()


tencent = Tencent()
