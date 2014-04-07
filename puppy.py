import urllib.request
import sys
import socket


def find_admin_login(url) :

  success_res = ['200', '500', '301', '302']
  web_apps = ['php', 'asp', 'jsp', 'aspx']

  with open('dict/admin_long.txt', 'r') as file_content:
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
  counter = ''
  for request_url in request_urls :
    sys.stdout.write("\b" * len(counter))
    counter = 'Searching: (' + str(i) + '/' + str(total_urls) + ')'
    i += 1
    try:
      request = urllib.request.Request(request_url)
      response = urllib.request.urlopen(request, timeout = 3)
      if str(response.status) in success_res :
        print(str(response.status) + ' ' + request_url)
    except urllib.error.HTTPError as e:
      if str(e.code) in success_res :
        print(str(e.code) + ' ' + request_url)
    except socket.timeout as e:
      continue
    print(counter, end = '\r')

  return response.status


target_url = input('Target URL: ')
operate = 100

while isset int(operate) != 0:

  print ('''
  1. Find Admin Login.
  0. Exit.
  ''')

  operate = input('Chose Operate: ')
  switch
  pass

# find_admin_login(target_url);
