# pip と setuptoolsの更新
# python -m pip install --upgrade pip setuptools


import urllib3 
import json 

'''
url0 = 'https://example.com/'
url1 = 'https://www.deepl.com/ja/translator#ja/en/この文章を翻訳する'
url2 = 'https://www.deepl.com/ja/translator#ja/en/%E3%81%93%E3%81%AE%E6%96%87%E7%AB%A0%E3%82%92%E7%BF%BB%E8%A8%B3%E3%81%99%E3%82%8B'


http = urllib3.PoolManager() 

r = http.request('GET', url0) 
 
print(json.dumps(dict(r.headers), ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))
'''

'''
from urllib import request

# url = 'https://www.deepl.com/ja/translator#ja/en/%E3%81%93%E3%81%AE%E6%96%87%E7%AB%A0%E3%82%92%E7%BF%BB%E8%A8%B3%E3%81%99%E3%82%8B'
url = 'https://www.deepl.com/ja/translator#ja/en/この文章を翻訳する'
response = request.urlopen(url)
content = response.read()
response.close()
html = content.decode()

# title = html.split('<title>')[1].split('</title')[0]
# print(html)
'''