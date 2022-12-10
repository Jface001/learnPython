# @Time : 2022/11/28 23:36 
# @Author : Jface 
# @coding: utf8
# url 解析练习
import urllib.parse as urlparse

url = 'https://item.jd.com/100026959232.html?cu=true&utm_source=www.linkstars.com&utm_medium=tuiguang&utm_campaign' \
      '=t_1000089893_156_0_184__57d73cbcea36f78b&utm_term=33f81ac7b49d4d6e955d63cf87b48688 '
parsed = urlparse.urlparse(url)
qs = urlparse.parse_qs(parsed.query)

res = {k: v[0] for k, v in qs.items()}
print(res)

