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

data = [(1, "A towel,", 1.0),
        (42, " it says, ", 2.0),
        (1337, "is about the most ", -1),
        (0, "massively useful thing ", 123),
        (-2, "an interstellar hitchhiker can have.", 3)]

# Write CSV file
kwargs = {'newline': ''}
mode = 'w'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'wb'

with open('test.csv', mode, **kwargs) as fp:
    writer = csv.writer(fp, delimiter=str(','))
    # writer.writerow(["your", "header", "foo"])  # write header
    writer.writerows(data)

# Read CSV file
kwargs = {'newline': ''}
mode = 'r'
if sys.version_info < (3, 0):
    kwargs.pop('newline', None)
    mode = 'rb'
with open('test.csv', mode, **kwargs) as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

print(data_read)

# Write CSV file
with open('test.csv', 'w', newline='') as fp:
    writer = csv.writer(fp, encoding='utf-8')
    # writer.writerow(["your", "header", "foo"])  # write header
    writer.writerows(data)