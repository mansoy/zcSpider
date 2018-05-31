import requests
import random
from scrapy.selector import Selector

IPPools = []

class MsIps:
    def __init__(self):
        #self.IPPools = []
        pass

    def checkProxy(self, proxy):
        url = "https://www.baidu.com/"
        try:
            proxy_dict = {
                "http": proxy,
            }
            response = requests.get(url=url, proxies=proxy_dict)
            code = response.status_code
            if code >= 200 and code < 300:
                print("链接成功[{0}]".format(proxy_dict))
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def getIps(self, pagecount = 20):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
        for page in range(1, pagecount):
            try:
                url = 'http://www.xicidaili.com/nn/{0}'.format(page)
                response = requests.get(url, headers=headers)
                datas = Selector(text=response.text).xpath('//table[@id="ip_list"]//tr[@class]').extract()
                for data in datas:
                    try:
                        vNodes = Selector(text=data).xpath('//div[@class="bar"]/@title').extract()
                        speed1 = float(vNodes[0].strip('秒'))
                        speed2 = float(vNodes[1].strip('秒'))
                        #if (speed1 > 1.0) or (speed2 > 1.0):
                        #    continue
                        vNodes = Selector(text=data).xpath('//td/text()').extract()
                        sProxy = '{0}://{1}:{2}'.format(vNodes[5], vNodes[0], vNodes[1])
                        print(sProxy)
                        if self.checkProxy(sProxy):
                            IPPools.append(sProxy)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    msIps = MsIps()
    msIps.getIps()


                



