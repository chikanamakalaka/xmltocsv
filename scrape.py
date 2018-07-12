#!/usr/bin/env python

from lxml import html
import requests
page = requests.get('video.html')
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