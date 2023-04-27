import json
import requests
import re

headers = {
    'authority': 'www.youtube.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"112.0.5615.138"',
    'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

response = requests.get('https://www.youtube.com/feed/guide_builder', headers=headers).text
re_html = re.compile('"content":(.*),"tabIdentifier":', re.S)
o = re_html.findall(response)[0]
dic_dic = json.loads(o)
li = dic_dic['sectionListRenderer']['contents'][7]
title = li['itemSectionRenderer']['contents'][0]['shelfRenderer']['title']['runs']
html_li = li['itemSectionRenderer']['contents'][0]['shelfRenderer']['content']['horizontalListRenderer']['items']
print(title)
for i in html_li:
    print(i['gridChannelRenderer']['title'])
    print(i['gridChannelRenderer']['subscriberCountText']['simpleText'])
    print('https://www.youtube.com' +
          i['gridChannelRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'] + '/about')
    print('*' * 30)

