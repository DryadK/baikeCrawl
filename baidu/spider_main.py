# coding:utf-8
# 爬虫总调度程序

# 编写入口URL
from baidu import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    # 初始化各个模块
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                # 判断爬取数量
                if count == 100:
                    break
                new_url = self.urls.get_new_url()
                print 'Crawl %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1
            except:
                print('Crawl Failed %d' % (count))

        self.outputer.output_html()

if __name__ == "__main__":
    url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.crawl(url)
