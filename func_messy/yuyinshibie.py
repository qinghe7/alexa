import urllib.parse, urllib.request
import time
import json
import hashlib
import base64
from aip import AipSpeech

# 百度
app_id = '20249073'
api_key = 'PG3YiRa3P6ffaLoModRrHc6w'
sceret_key = 'hX72G4wYMLNU878i2VhtDpncBuvxPW7d'
client = AipSpeech(app_id, api_key, sceret_key)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
	
def baidu(file):
	#print('百度语音为您服务')
	result = client.asr(get_file_content(file), 'wav', 16000, {'lan': 'zh',})
	print(result)
	return result
