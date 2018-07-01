from scrapy import Spider, Request, FormRequest


class SpiderNgaSpider(Spider):
    name = 'spider_nga'
    allowed_domains = ['bbs.ngacn.cc']
    start_urls = ['http://bbs.ngacn.cc/thread.php?fid=-7']

    # =================================================== #

    # 页码
    page_num = 1
    # 搜索关键字
    param = ""
    # 是否自动回复标识
    flag = 0
    # 爬虫类型
    type = 0
    # 指定楼层
    floor = 0

    # =================================================== #

    def start_requests(self):
        self.type = input("0:随机爬       1:指定贴抢楼")

        # 随机爬
        if self.type == '0':
            self.param = input("输入想要搜索的关键字:")
            self.flag = input("是否需要自动回复（0:no  ====  1:yes）:")
            # 这里带着cookie发出请求
            yield Request(url=self.start_urls[0], cookies=self.settings['COOKIE'])

        # 指定爬
        if self.type == '1':
            # 指定帖url
            specified_url = input("指定贴url:")
            # 指定楼层
            self.floor = input("指定楼层:")
            # 跟进指定url
            yield Request(specified_url, cookies=self.settings['COOKIE'],
                          callback=self.detail_parse)

    # 列表分析
    def parse(self, response):
        self.page_num = self.page_num + 1
        # 当前页所有的帖子
        contents = response.xpath("//table//tr[contains(concat(' ', @class, ' '), 'topicrow')]")

        for content in contents:
            # 获取每个帖子的信息
            reply_num = content.xpath(".//td[@class='c1']/a/text()").extract()[0]
            title = content.xpath(".//td[@class='c2']/a/text()").extract()[0]
            url = content.xpath(".//td[@class='c2']/a/@href").extract()[0]
            uid = content.xpath(".//td[@class='c3']/a/@title").extract()[0]

            # 判断帖子是否包含指定字符
            if self.param in title:
                # print(title + "    ======    " + url)
                # 跟进帖子
                yield Request('http://bbs.ngacn.cc' + url, cookies=self.settings['COOKIE'],
                              callback=self.detail_parse)

        # 当前页爬完，进入下一页
        yield Request('http://bbs.ngacn.cc/thread.php?fid=-7&page=' + str(self.page_num),
                      cookies=self.settings['COOKIE'],
                      callback=self.parse)

    # 帖子详情分析以及回复
    def detail_parse(self, response):
        if self.type == '0':
            # 标题
            content = response.xpath("//h3[@id='postsubject0']/text()").extract()[0]

            # 过滤抽取url
            tid_fid = response.xpath("//div[@id='postbbtm']/a/@href").extract()[0][26:]
            tid_fid = tid_fid.split("&tid=")

            # 截取tid，fid
            fid = tid_fid[0]
            tid = tid_fid[1]

            print(content + "       tid:" + tid + "====== fid:" + fid)
            # 回帖，回调判断成功与否
            if self.flag == '1':
                yield FormRequest(url='http://bbs.ngacn.cc/post.php', cookies=self.settings['COOKIE'],
                                  formdata={"action": "reply", "fid": fid, "tid": tid, "post_content": content,
                                            "nojump": "1", "lite": "htmljs", "step": "2"}, callback=self.post_status)
        pass

    def post_status(self, response):
        print(response.status)
        pass

    def xpath_helper(self, response, xpath_detail, if_extract=False, index=-1):
        # 如果需要
        if if_extract and index >= 0:
            return response.xpath(xpath_detail).extract()[index]
        if if_extract:
            return response.xpath(xpath_detail).extract()
        if not if_extract:
            return response.xpath(xpath_detail)
