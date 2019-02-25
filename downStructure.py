# -*- coding: utf-8 -*-
import os
import re
import traceback

helpmsg ='''------------
!!getStructure <URL> -下载结构文件到本地
------------'''

def onServerInfo(server, info):
  if info.isPlayer == 1:
    if info.content.startswith('!!getStructure'):
      if info.content == '!!getStructure':
        for line in helpmsg.splitlines():
          server.tell(info.player, line)
      elif info.content.startswith == '!!getStructure dir ':
        try:
          for i in os.listdir(info.content.split(' ')[2]):
            server.tell(info.player, i)
        except:
          lines = traceback.format_exc().splitlines()
          for l in lines:
            server.say(l)
