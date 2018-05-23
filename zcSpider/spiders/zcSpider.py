import scrapy
import arrow
import json
import logging

from datetime import datetime
from scrapy.http import Request
from scrapy.selector import Selector
from zcSpider.comm import zcString
from zcSpider.comm import zcTools
from zcSpider.items import MatchDataItem
from zcSpider.items import OuOddsItem
from zcSpider.items import YaOddsItem
from zcSpider.items import YaOddsDetailItem


headers = {

    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN',
    'Connection': 'Keep-Alive',
    #'Cookie': 'sdc_session=1526983196230; Hm_lpvt_4f816d475bb0b9ed640ae412d6b42cab=1526983410; motion_id=1526983280925_0.27740046278176144; ck_RegUrl=trade.500.com; _jzqc=1; __utmc=63332592; __utmz=63332592.1526983258.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ck_RegFromUrl=http%3A//trade.500.com/jczq/%3Fdate%3D2018-01-20; sdc_userflag=1526983196230::1526983410123::4; _jzqb=1.3.10.1526983200.1; __utma=63332592.1440787636.1526983258.1526983258.1526983258.1; Hm_lvt_4f816d475bb0b9ed640ae412d6b42cab=1526983196; _jzqckmp=1; __utmb=63332592.4.10.1526983258; _jzqa=1.783733940908145800.1526983200.1526983200.1526983200.1; CLICKSTRN_ID=123.139.29.83-1526983193.265753::9875C9DED126466E2ABB227B342F9969; __utmt=1; _jzqx=1.1526983200.1526983200.1.jzqsr=trade%2E500%2Ecom|jzqct=/jczq/.-; _qzjc=1; Hm_lpvt_40a8e2d10b0aab8fc5816be65a102f0c=1526983283; WT_FPC=id=undefined:lv=1526983410122:ss=1526983201635; _qzjb=1.1526983200555.3.0.0.0; Hm_lvt_40a8e2d10b0aab8fc5816be65a102f0c=1526983202,1526983283; _qzjto=3.1.0; _qzja=1.65817644.1526983200555.1526983200555.1526983200555.1526983282971.1526983410237.0.0.0.3.1; bdshare_firstime=1526983200078',
    'Host': 'odds.500.com',
    'User-Agent': 'Mozilla/5.0 (MSIE 9.0; qdesk 2.5.1277.202; Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}


class zcSpider(scrapy.Spider):
    name = 'zcSpider'
    allowed_domains = ['500.com']
    base_url = 'http://trade.500.com/jczq/?date='

    def start_requests(self):
        start = datetime(2018, 1, 1)
        end = datetime(2018, 2, 1)
        for day in arrow.Arrow.range('day', start, end):
            url = self.base_url + day.format('YYYY-MM-DD')
            yield Request(url, self.parse, meta={'year': day.format('YYYY'), 'date': day.format('YYYY-MM-DD')})
        #url = self.base_url + '2010-01-20'
        #yield Request(url, callback=self.parse, meta={'year': '2018'})

        #url = 'http://odds.500.com/fenxi1/yazhi.php?id=680508&ctype=1&start=30&r=1&style=0&guojia=0'
        #yield Request(url=url, callback=self.parseYpData, meta={'mid': '680508', 'year': '2010'})

    def parse(self, response):
        if response.status == 200:
            datas = Selector(response).xpath('//tr[@isend="1"]').extract()
            for data in datas:
                try:
                    st = Selector(text=data)
                    item = MatchDataItem()
                    item['mid'] = st.xpath('//tr/@fid').extract()[0]
                    item['mlmName'] = st.xpath('//tr/@lg').extract()[0]
                    item['mmTeam'] = st.xpath('//tr/@homesxname').extract()[0].replace(' ', '')
                    item['mdTeam'] = st.xpath('//tr/@awaysxname').extract()[0].replace(' ', '')
                    item['mIsend'] = st.xpath('//tr/@isend').extract()[0]
                    item['mDate'] = st.xpath('//tr/@pdate').extract()[0]
                    item['mWeek'] = st.xpath('//tr/@gdate').extract()[0]
                    item['mSell'] = st.xpath('//tr/@pendtime').extract()[0]

                    # 提取比赛得分
                    tmpNode = st.xpath('//a[@class="score"]/text()').extract()
                    if len(tmpNode) > 0:
                        clst = tmpNode[0].split(':')
                        item['mQj'] = int(clst[0])  # 进球数
                        item['mQs'] = int(clst[1])  # 失球数
                        item['mWinStatus'] = zcTools.fb_kwin4qnum(int(clst[0]), int(clst[1]))
                    else:
                        item['mQj'] = -1
                        item['mQs'] = -1
                        item['mWinStatus'] = -1

                    item['mRWinStatus'] = -1

                    # 提取让球数

                    try:
                        tmpNode = st.xpath('//span[@class="eng green"] or @class="eng red"]/text()').extract()
                        item['mQr'] = int(tmpNode[0])
                    except:
                        item['mQr'] = '0'

                    # 提取主队编号
                    tmpNode = st.xpath('//td[@class="left_team"]/a/@href').extract()
                    item['mmTeamId'] = zcString.str_xmid(tmpNode[0], '/team/', '/')

                    # 提取客队编号
                    tmpNode = st.xpath('//td[@class="right_team"]/a/@href').extract()
                    item['mdTeamId'] = zcString.str_xmid(tmpNode[0], '/team/', '/')

                    # 提取比赛时间
                    item['mTime'] = st.xpath('//span[@class="match_time"]/text()').extract()[0]

                    yield item

                    # 欧赔页面url
                    url = 'http://odds.500.com/fenxi/ouzhi-' + item['mid'] + '.shtml'
                    yield Request(url=url, callback=self.getOpData, meta={'mid': item['mid']})

                    # 亚赔页面url
                    url = 'http://odds.500.com/fenxi/yazhi-' + item['mid'] + '.shtml'
                    yield Request(url=url, callback=self.getYpData,
                                  meta={'mid': item['mid'], 'year': response.meta['year'], 'date': response.meta['date']})
                    # print(item)
                except Exception as e:
                    self.log('[Parse Error][{0}]HomePage Error[{1}]'.format(response.meta['date'], e))
        else:
            self.log('[Status Error][{0}]HomePage Status[{1}]'.format(response.meta['date'], response.status))


    # 获取欧赔数据
    def getOpData(self, response):
        mid = response.meta['mid']
        spdate = response.meta['date']
        try:
            if response.status == 200:
                tmpNode = Selector(response=response).xpath(
                    '//div[@class="table_btm"]//span[@id="nowcnum"]/text()').extract()
                lyCount = int(tmpNode[0])
                pageCount = lyCount // 30 + (1 if lyCount % 30 > 0 else 0)
                for i in range(pageCount):
                    url = 'http://odds.500.com/fenxi1/ouzhi.php?id={0}&ctype=1&start={1}&r=1&style=0' \
                          '&guojia=0&chupan=1'.format(mid, i * 30)
                    #print('getOpData[{0}]pageCount[{1}]Index[{2}]'.format(mid, pageCount, i))
                    yield Request(url=url, callback=self.parseOpData, meta={'mid': mid, 'date': spdate})
            else:
                self.log('[Status Error][{0} - {1}]OuOdds Status[{1}]'.format(spdate, mid, response.status))
        except Exception as e:
            self.log('[Parse Error][{0} - {1}]GetOuOdds Error{1}'.format(spdate, mid, e))

    # 解析欧赔一页数据
    def parseOpData(self, response):
        mid = response.meta['mid']
        spdate = response.meta['date']
        if response.status == 200:
            datas = Selector(response).xpath('//tr[@ttl="zy"]').extract()
            for data in datas:
                try:
                    item = OuOddsItem()
                    st = Selector(text=data)
                    # 提取博彩公司名称
                    lmName = st.xpath('//td[@class="tb_plgs"]/@title').extract()[0]
                    lmName.replace(' ', '')

                    item['mid'] = mid
                    item['mlyName'] = lmName
                    # 提取数据(20个数据一次按顺序对应相关数据)
                    numdatas = st.xpath('////table[@class="pl_table_data"]//tr/td/text()').extract()

                    # 即时赔率
                    item['mOdds11'] = float(numdatas[0].strip())
                    item['mOdds12'] = float(numdatas[1].strip())
                    item['mOdds13'] = float(numdatas[2].strip())

                    item['mOdds21'] = float(numdatas[3].strip())
                    item['mOdds22'] = float(numdatas[4].strip())
                    item['mOdds23'] = float(numdatas[5].strip())

                    # 即时概率
                    item['mChance11'] = float(numdatas[6].strip().replace('%', ''))
                    item['mChance12'] = float(numdatas[7].strip().replace('%', ''))
                    item['mChance13'] = float(numdatas[8].strip().replace('%', ''))

                    item['mChance21'] = float(numdatas[9].strip().replace('%', ''))
                    item['mChance22'] = float(numdatas[10].strip().replace('%', ''))
                    item['mChance23'] = float(numdatas[11].strip().replace('%', ''))

                    # 返还率
                    item['mRetRatio1'] = float(numdatas[12].strip().replace('%', ''))
                    item['mRetRatio2'] = float(numdatas[13].strip().replace('%', ''))

                    # 即时凯利
                    item['mKaili11'] = float(numdatas[14].strip())
                    item['mKaili12'] = float(numdatas[15].strip())
                    item['mKaili13'] = float(numdatas[16].strip())

                    item['mKaili21'] = float(numdatas[17].strip())
                    item['mKaili22'] = float(numdatas[18].strip())
                    item['mKaili23'] = float(numdatas[19].strip())

                    yield item
                except Exception as e:
                    self.log('[Parse Error][{0} - {1}]Parse OuOdds Error{1}'.format(spdate, mid, e))
        else:
            self.log('[Status Error][{0} - {1}]Parse OuOdds Status[{1}]'.format(spdate, mid, response.status))

    # 获取亚赔数据
    def getYpData(self, response):
        mid = response.meta['mid']
        year = response.meta['year']
        spdate = response.meta['date']
        try:
            if response.status == 200:
                tmpNode = Selector(response=response).xpath('//div[@class="table_btm"]//span[@id="nowcnum"]/text()').extract()
                lyCount = int(tmpNode[0])
                pageCount = lyCount // 30 + (1 if lyCount % 30 > 0 else 0)
                for i in range(pageCount):
                    url = 'http://odds.500.com/fenxi1/yazhi.php?id={0}&ctype=1&start={1}&r=1&' \
                          'style=0&guojia=0'.format(mid, i * 30)
                    #print('getYpData[{0}]pageCount[{1}]Index[{2}]'.format(mid, pageCount, i))
                    yield Request(url=url, callback=self.parseYpData, meta={'mid': mid, 'year': year, 'date': spdate})
            else:
                self.log('[Status Error][{0} - {1}]YaOdds Status[{1}]'.format(spdate, mid, response.status))
        except Exception as e:
            print('{0}解析博彩公司数量时发生错误{1}'.format(mid, e))
            self.log('[Parse Error][{0} - {1}]GetOuOdds Error{1}'.format(spdate, mid, e))


    # 解析亚盘数据
    def parseYpData(self, response):
        datas = Selector(response).xpath('//tr[@xls="row"]').extract()
        mid = response.meta['mid']
        year = response.meta['year']
        spdate = response.meta['date']
        if response.status == 200:
            for data in datas:
                try:
                    item = YaOddsItem()
                    st = Selector(text=data)
                    item['mid'] = mid

                    # 提取博彩公司名称
                    lmName = st.xpath('//span[@class="quancheng"]/text()').extract()[0]
                    item['mlyName'] = lmName.replace(' ', '')

                    oddss = st.xpath('//tr[@xls="row"]//table[@class="pl_table_data"]').extract()

                    # 提取即时盘口数据
                    tds = Selector(text=oddss[0]).xpath('//td/text()').extract()
                    item['mImmOdds1'] = float(tds[0].replace('↑', '').replace('↓', ''))
                    item['mImmDisc'] = tds[1]
                    item['mImmOdds2'] = float(tds[2].replace('↑', '').replace('↓', ''))
                    item['mImmStatus'] = 1

                    tmpNode = st.xpath('//td[@class="ying"]/text()').extract()
                    if len(tmpNode) > 0:
                        if tmpNode[0] == tds[2]:
                            item['mImmStatus'] = 2

                    # 提取初始盘口数据
                    tds = Selector(text=oddss[1]).xpath('//td/text()').extract()
                    item['mInitOdds1'] = float(tds[0].replace('↑', '').replace('↓', ''))
                    item['mInitDisc'] = tds[1]
                    item['mInitOdds2'] = float(tds[2].replace('↑', '').replace('↓', ''))

                    oddsTimes = st.xpath('//time/text()').extract()
                    # 即时盘口变化时间
                    item['mImmDate'] = '{0}-{1}'.format(year, oddsTimes[0])
                    # 初始盘口变化时间
                    item['mInitDate'] = '{0}-{1}'.format(year, oddsTimes[0])

                    item['mmyId'] = st.xpath('//tr/@id').extract()[0]
                    item['mDtDate'] = st.xpath('//tr/@dt').extract()[0]

                    yield item

                    # 解析明细数据
                    url = 'http://odds.500.com/fenxi1/inc/ajax.php?t=yazhi&p=1&r=1&fixtureid={0}&companyid={1}&updatetime={2}'.format(mid, item['mmyId'], item['mDtDate'])
                    yield Request(url=url, callback=self.parseYpDetailData, meta={'mid': mid, 'lyName': item['mlyName'], 'date': spdate})
                except Exception as e:
                    self.log('[Parse Error][{0} - {1}]Parse YaOdds Error{1}'.format(spdate, mid, e))
        else:
            self.log('[Status Error][{0} - {1}]Parse YaOdds Status[{1}]'.format(spdate, mid, response.status))


    def parseYpDetailData(self, response):
        mid = response.meta['mid']
        lyName = response.meta['lyName']
        spdate = response.meta['date']
        try:
            if response.status == 200:
                datas = json.loads(response.body)
                for key, data in enumerate(datas):
                    if key == 0: continue
                    item = YaOddsDetailItem()
                    item['mid'] = mid
                    item['mlyName'] = lyName
                    item['mOdds1'] = float(data[0])
                    item['mDisc'] = data[1]
                    item['mOdds2'] = float(data[2])
                    yield item
            else:
                self.log('[Status Error][{0} - {1}]Parse YaOdds Details Status[{1}]'.format(spdate, mid, response.status))
        except Exception as e:
            self.log('[Parse Error][{0} - {1}]Parse YaOdds Details Error{1}'.format(spdate, mid, e))
