# coding:utf-8
# html页面下载器
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return "!200"
        return response.read()

