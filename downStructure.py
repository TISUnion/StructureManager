# -*- coding: utf-8 -*-
import os
import re

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
        for i in info.content.split(' ')[2]:
          server.tell(info.player, i)
