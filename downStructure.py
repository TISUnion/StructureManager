# -*- coding: utf-8 -*-
import os
import re
import urllib2
import traceback

helpmsg ='''------------
!!structget <folder> <name> <url> (-o) (-b64) -下载结构文件到本地的文件夹中
请指定文件夹，以免覆盖同名结构文件
文件夹和文件名只兼容英文大小写字母、数字和下划线
使用 -o 在重名时覆盖
使用 -b64 打开base64模式，将会作为base64编码的文件被下载和解码
!!structget -l (<foldername>) -列出服务器的结构文件
指定文件夹名进一步定位
------------'''

def onServerInfo(server, info):
  try:
    if info.isPlayer == 1:
        if info.content.startswith('!!structget'):
            if info.content == '!!structget':
                for line in helpmsg.splitlines():
                    server.tell(info.player, line)
            elif re.match('^!!structget -l( \w+)?$', info.content):
                args = info.content.split(' ')
                if len(args) == 3:
                    listStruct(server, info.player, args[2])
                else:
                    listStruct(server, info.player)
            elif re.match('^!!structget \w+ \w+ \S+( -o)?( -b64)?( -o)?$', info.content)
                args = info.content.split(' ')
                can_overwrite = info.content.find(' -o') > -1
                if info.content.find(' -b64') > -1:
                    getStruct(args[1], args[2], args[3], can_overwrite)
                else
                    getStructB64(args[1], args[2], args[3], can_overwrite)
  except:
    lines = traceback.format_exc().splitlines()
    for l in lines:
        server.say(l)
                     
def getStruct(server, foldername, filename, url, can_overwrite):
#     result = os.system('cd server\world\generated\ && wget -N ' + args[1])
#         if result == 0:
#           server.say('success')
#         else:
#           server.say('failed to download')
    pass
    
def getStructB64(server, foldername, filename, url, can_overwrite):
    pass

def listStruct(server, player):
    g = os.walk('\server\world\generated')
    for i in next(g)[1]:
        for j in next(g)[2]:
            server.tell(player, i + ':' + j.replace('.nbt',''))

def listStruct(server, player, foldername):
    pass
