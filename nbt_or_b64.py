from base64 import encode, decode
from sys import argv

filename = argv[1]
print(filename)
if filename.endswith('.nbt'):
  with open(filename,'rb') as nbtfile:
    with open(filename[0:len(filename)-4]+'_b64encoded.txt','wb') as b64file:
      encode(nbtfile,b64file)
elif filename.endswith('.txt'):
  with open(filename,'rb') as b64file:
    with open(filename[0:len(filename)-4]+'_b64decoded.nbt','wb') as nbtfile:
      decode(b64file,nbtfile)
