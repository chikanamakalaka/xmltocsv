#!/usr/bin/env python

from lxml import html
import requests
import os
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

#Get Section headers
group = tree.xpath('/html/body/div/div/div[2]/main/section[@id = "content"]/div[@id = "block-gravit-content"]/article[@id = "node-1181"]/div/section[2]/h3')

#Get list of video urls
video = tree.xpath('/html/body/div/div/div[2]/main/section[@id = "content"]/div[@id = "block-gravit-content"]/article[@id = "node-1181"]/div/section[2]/div/section[1]/div/div[1]/div/iframe')

#Get list of Video titles
titles = tree.xpath('/html/body/div/div/div[2]/main/section[@id = "content"]/div[@id = "block-gravit-content"]/article[@id = "node-1181"]/div/section[2]/div/section[1]/div/div[2]/div')

#Get list of Video discriptions
disc = tree.xpath('/html/body/div/div/div[2]/main/section[@id = "content"]/div[@id = "block-gravit-content"]/article[@id = "node-1181"]/div/section[2]/div/section[1]/div/div[3]/div/p')

print 'Group: ', group
print 'Video URL: ', video
print 'Title: ', titles
print 'Discription: ', disc