# -*- coding: utf-8 -*-
import os

helpmsg ='''------------
!!getStructure <URL> -下载结构文到本地
------------'''

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!getStructure'):
      if (len(args) == 1):
        for i in os.listdir('../'):
          server.say(i)
