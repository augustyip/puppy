#!/usr/bin/env python

import urllib.request
import urllib.parse

import json

from lib.core.data import config


def quotes() :

  endpoint = config['Yahoo']['endpoint'] + '?'
  # endpoint = 'https://query.yahooapis.com/v1/public/yql?'

  stocks = ['"' + stock.strip() + '"' for stock in config['Default']['stocks'].split(',')]

  yql = 'select * from yahoo.finance.quotes where symbol in (' + ','.join(stocks) + ')'

  params = {
    'q' : yql,
    'format' : config['Yahoo']['format'],
    'env' : config['Yahoo']['env'],
    'diagnostics' : config['Yahoo']['diagnostics']
  }

  query_url = endpoint+ urllib.parse.urlencode(params)

  request = urllib.request.Request(query_url)
  request.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0')

  try :
    response = urllib.request.urlopen(request, timeout = 3)
    query_result = json.loads(response.read().decode("utf-8"))


    if len(query_result['query']['results']['quote']) > 0 :
      return query_result['query']['results']['quote']

  except :
    quotes()

