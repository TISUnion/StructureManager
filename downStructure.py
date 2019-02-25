# -*- coding: utf-8 -*-
import os
import re
import urllib2
import traceback

helpmsg ='''------------
!!getStructure <folder> <URL> -下载结构文件到本地的文件夹中
请指定文件夹，以免覆盖同名结构文件
------------'''

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!structget'):
      if info.content == '!!structget':
        for line in helpmsg.splitlines():
          server.tell(info.player, line)
      elif re.match('!!structget \w+ \S+', info.content)
        args = info.content.split(' ')
        getFile()
                     
def getFile()
