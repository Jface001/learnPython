# @Time : 2022/11/29 00:16 
# @Author : Jface 
# @coding: utf8
# 爬取豆瓣电影排行
import json

import requests

url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type': '5',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}
response = requests.get(url=url, params=params, headers=header)
content = response.json()
# 在使用dumps时候，会默认将汉子转成ascii编码格式，因此我们需要手动设置成False
content1 = json.dumps(content, ensure_ascii=False)
print(content1)
