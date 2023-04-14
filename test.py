from requests_html import HTMLSession
session = HTMLSession()
# 获取网页
r = session.get("https://news.cnblogs.com/n/recommend")
# 通过CSS找到新闻标签

news = r.html.find('h2.news_entry > a')
for new in news:
    print(new.text)  # 获得新闻标题
    print(new.absolute_links)  # 获得新闻链接
