#!/usr/bin/env python

from lxml import html
import requests
import os
import unicodecsv as csv
import sys
from requests_testadapter import Resp

class LocalFileAdapter(requests.adapters.HTTPAdapter):
    def build_response_from_file(self, request):
        file_path = request.url[7:]
        with open(file_path, 'rb') as file:
            buff = bytearray(os.path.getsize(file_path))
            file.readinto(buff)
            resp = Resp(buff)
            r = self.build_response(request, resp)

            return r

    def send(self, request, stream=False, timeout=None,
             verify=True, cert=None, proxies=None):

        return self.build_response_from_file(request)

requests_session = requests.session()
requests_session.mount('file://', LocalFileAdapter())

page = requests_session.get('file:///Users/mhocker/Desktop/xmltocsv/video.html')
tree = html.fromstring(page.content)

# #Get Section headers
group = tree.xpath('/html/body/div/div/div/main/section/div/article/div/section/h3/text()')

#Get list of video urls
video_url = tree.xpath('/html/body/div/div/div/main/section/div/article/div/section/div/section/div/div/div/iframe/@src')

#Get list of Video titles
title = tree.xpath('/html/body/div/div/div/main/section/div/article/div/section/div/section/div/div/div/text()')

#Get list of Video discriptions
desc = tree.xpath('/html/body/div/div/div/main/section/div/article/div/section/div/section/div/div/div/p/text()')

# Write CSV file
kwargs = {'newline': ''}
mode = 'w'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'wb'

with open('test.csv', mode, **kwargs) as fp:
    writer = csv.writer(fp, delimiter=str(','))
    writer.writerow(["group", "video_url", "title", "desc"])  # write header
    writer.writerows(group)
    writer.writerows(video_url)
    writer.writerows(title)
    writer.writerows(desc)

# Read CSV file
kwargs = {'newline': ''}
mode = 'r'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'rb'
with open('test.csv', mode, **kwargs) as fp:
    reader = csv.reader(fp, delimiter=';', quotechar='"')
    next(reader, None)  # skip the headers
    data_read = [row for row in reader]

print(data_read)

