# coding:utf-8
# url管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  # 待爬取
        self.old_urls = set()  # 已爬取

    # 添加一个新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)


    # 添加多个新的url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断是否存在待爬取url
    def has_new_url(self):
        return self.new_urls != 0

    # 从管理器中获取新的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

