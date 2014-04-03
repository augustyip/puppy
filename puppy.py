import urllib.request
import sys
import socket

success_res = ['200', '500', '301', '302', '403']
web_apps = ['php', 'asp', 'jsp']

def find_admin_login(url) :
  global success_res
  global web_apps

  with open('dict/admin_short.txt', 'r') as file_content:
    admin_context_paths = file_content.read().split('\n')

  request_urls = []


  for path in admin_context_paths:
    path.strip()
    if len(path) == 0 :
      continue

    if '{ext}' in path :
      for web_app in web_apps:
        replaced_path = path.replace('{ext}', web_app)
        request_url = url + replaced_path if url.endswith('/') else url + '/' + replaced_path
        request_urls.append(request_url)
    else :
      request_url = url + path if url.endswith('/') else url + '/' + path
      request_urls.append(request_url)

  total_urls = len(request_urls)
  i = 1

  for request_url in request_urls :
    counter = 'Searching: ' + str(i) + '/' + str(total_urls)
    try:
      request = urllib.request.Request(request_url)
      response = urllib.request.urlopen(request, timeout = 3)
      if str(response.status) in success_res :
        sys.stdout.write("\b" * len(counter))
        print(str(response.status) + ' ' + request_url)
    except urllib.error.HTTPError as e:
      if str(e.code) in success_res :
        sys.stdout.write("\b" * len(counter))
        print(str(e.code) + ' ' + request_url)
    except socket.timeout as e:
      e
    print(counter, end='\r')
    i += 1

  return response.status

url = 'http://delbert.me/'
find_admin_login(url);
