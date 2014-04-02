import urllib.request
import re

success_res = ['200', '500', '301', '302', '403']
web_apps = ['php', 'asp', 'jsp']

def main(url) :
  global success_res
  global web_apps

  with open('data/admins.txt', 'r') as file_content:
    admin_context_paths = file_content.read().split('\n')

  for path in admin_context_paths:
    # path = re.sub('/\s\s+/', ' ', path)
    path.rstrip()
    # pattern = re.compile(r'\s+')
    # path = re.sub(pattern, '', path)
    if '%EXT%' in path :
      for web_app in web_apps:
        replaced_path = path.replace('%EXT%', web_app)
        request_url = url + replaced_path if url.endswith('/') else url + '/' + replaced_path
        try:
          request = urllib.request.Request(request_url)
          response = urllib.request.urlopen(request, timeout = 3)
          if str(response.status) in success_res :
            print (str(response.status) + ' ' + request_url)
        except urllib.error.HTTPError as e:
          if str(e.code) in success_res :
            print (str(e.code) + ' ' + request_url)
    else :
      request_url = url + path if url.endswith('/') else url + '/' + path
      try:
        request = urllib.request.Request(request_url)
        response = urllib.request.urlopen(request, timeout = 3)
        if str(response.status) in success_res :
          print (str(response.status) + ' ' + request_url)
      except urllib.error.HTTPError as e:
        if str(e.code) in success_res :
          print (str(e.code) + ' ' + request_url)

  return response.status

url = 'http://delbert.me/'
main(url);
