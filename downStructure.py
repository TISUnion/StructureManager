# -*- coding: utf-8 -*-
import os
import re
import urllib2
import traceback

helpmsg ='''------------
§7!!structget <folder> <name> <url> (-o) (-b64)§r -下载结构文件到本地的文件夹中
请指定文件夹，以免覆盖同名结构文件
文件夹和文件名只兼容英文小写字母、数字、短划线和下划线
使用 §7-o§r 在重名时覆盖
使用 §7-b64§r 打开base64模式，将会作为base64编码的文件被下载和解码
§7!!structget -l (<key>)§r -列出服务器的结构文件，最多一次20个
指定关键字 §7<key>§r 进一步定位
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
            elif re.match('^!!structget [a-z-_0-9]+ [a-z-_0-9]+ \S+( -o)?( -b64)?( -o)?$', info.content):
                args = info.content.split(' ')
                can_overwrite = info.content.find(' -o') > -1
                if info.content.find(' -b64') > -1:
                    getStructB64(server, args[1], args[2], args[3], can_overwrite)
                else:
                    getStruct(server, args[1], args[2], args[3], can_overwrite)
  except:
    lines = traceback.format_exc().splitlines()
    for l in lines:
        server.say(l)
                     
def getStruct(server, foldername, filename, url, can_overwrite):
    if not can_overwrite:
        if os.path.exists('server/world/generated/'+foldername+'/structures/'+filename+'.nbt'):
            server.say('§a'+foldername+':'+filename+'§r§c exists, use §r§7-o§r§c to overwrite§r')
            return
    try:
        os.makedirs('server/world/generated/'+foldername+'/structures')
    except:
        pass
    result = os.system('cd server/world/generated/'+foldername+'/structures && wget -O '+filename+'.nbt -N '+url)
    if result == 0:
        server.say('§a'+foldername+':'+filename+'§r has been downloaded successfully')
    else:
        server.say('§cfailed to download§r, result='+str(result))
    
def getStructB64(server, foldername, filename, url, can_overwrite):
    b64data = urllib2.urlopen('https://pastebin.com/raw/PxuhMiWK').read()

def listStruct(server, player, kwrd=''):
    counter = 0
    for i in os.listdir('server/world/generated/'):
        for j in os.listdir('server/world/generated/'+i+'/structures'):
            strout = i+':'+j
            if strout.find(kwrd) > -1:
                server.tell(player, '§a'+strout[0:len(strout)-4]+'§r')

                counter += 1
                if counter > 20:
                    return
