# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MatchDataItem(scrapy.Item):
    # 比赛场次编号
    mid = scrapy.Field()
    # 联赛名称
    mlsName = scrapy.Field()
    # 联赛编号
    mlsId = scrapy.Field()
    # 主队名称
    mmTeam = scrapy.Field()
    # 主队编号
    mmTeamId = scrapy.Field()
    # 客队名称
    mdTeam = scrapy.Field()
    # 客队编号
    mdTeamId = scrapy.Field()
    # 比赛状态(1代表比赛完成, 被取消的比赛一直是0)
    mIsend = scrapy.Field()
    # 让球
    mQr = scrapy.Field()
    # 主队进球
    mQj = scrapy.Field()
    # 客队进球
    mQs = scrapy.Field()
    # 比赛胜负情况
    mWinStatus = scrapy.Field()
    # 让球胜负情况
    mRWinStatus = scrapy.Field()
    # 比赛星期换算
    mWeek = scrapy.Field()
    # 比赛日期
    mDate = scrapy.Field()
    # 比赛时间
    mTime = scrapy.Field()
    # 彩票截至销售时间
    mSell = scrapy.Field()


class OuOddsItem(scrapy.Item):
    # 比赛场次编号
    mid = scrapy.Field()
    # 博彩公司名称
    mlyName = scrapy.Field()
    # 博彩公司编号
    mlyId = scrapy.Field()
    # 即时欧赔
    mOdds11 = scrapy.Field()
    mOdds12 = scrapy.Field()
    mOdds13 = scrapy.Field()
    mOdds21 = scrapy.Field()
    mOdds22 = scrapy.Field()
    mOdds23 = scrapy.Field()
    # 即时概率
    mChance11 = scrapy.Field()
    mChance12 = scrapy.Field()
    mChance13 = scrapy.Field()
    mChance21 = scrapy.Field()
    mChance22 = scrapy.Field()
    mChance23 = scrapy.Field()
    # 返还率
    mRetRatio1 = scrapy.Field()
    mRetRatio2 = scrapy.Field()
    # 即时凯利
    mKaili11 = scrapy.Field()
    mKaili12 = scrapy.Field()
    mKaili13 = scrapy.Field()
    mKaili21 = scrapy.Field()
    mKaili22 = scrapy.Field()
    mKaili23 = scrapy.Field()


class YaOddsDetailItem(scrapy.Item):
    mid = scrapy.Field()
    mlyName = scrapy.Field()
    #mlyId = scrapy.Field()
    myoid = scrapy.Field()
    mOdds1 = scrapy.Field()
    mDisc = scrapy.Field()
    mOdds2 = scrapy.Field()

class YaOddsItem(scrapy.Item):
    # 比赛场次编号
    mid = scrapy.Field()
    # 一场比赛中的一个赔率编号(对应赔率公司)
    mmyId = scrapy.Field()
    #
    mDtDate = scrapy.Field()
    # 博彩公司名称
    mlyName = scrapy.Field()
    # 博彩公司编号
    mlyId = scrapy.Field()
    # 即时盘口
    mImmOdds1 = scrapy.Field()
    mImmDisc = scrapy.Field()
    mImmOdds2 = scrapy.Field()
    mImmDate = scrapy.Field()
    mImmStatus = scrapy.Field()
    # 初始盘口
    mInitOdds1 = scrapy.Field()
    mInitDisc = scrapy.Field()
    mInitOdds2 = scrapy.Field()
    mInitDate = scrapy.Field()
    # 明细数据(500彩票中的更多)
    mDetailData = scrapy.Field()


class SizeOddsDetailItem(scrapy.Item):
    mid = scrapy.Field()
    mlyName = scrapy.Field()
    #mlyId = scrapy.Field()
    msoid = scrapy.Field()
    mOdds1 = scrapy.Field()
    mDisc = scrapy.Field()
    mOdds2 = scrapy.Field()

class SizeOddsItem(scrapy.Item):
    # 比赛场次编号
    mid = scrapy.Field()
    # 一场比赛中的一个赔率编号(对应赔率公司)
    mmyId = scrapy.Field()
    #
    mDtDate = scrapy.Field()
    # 博彩公司名称
    mlyName = scrapy.Field()
    # 博彩公司编号
    mlyId = scrapy.Field()
    # 即时盘口
    mImmOdds1 = scrapy.Field()
    mImmDisc = scrapy.Field()
    mImmOdds2 = scrapy.Field()
    mImmDate = scrapy.Field()
    mImmStatus = scrapy.Field()
    # 初始盘口
    mInitOdds1 = scrapy.Field()
    mInitDisc = scrapy.Field()
    mInitOdds2 = scrapy.Field()
    mInitDate = scrapy.Field()
    # 明细数据(500彩票中的更多)
    mDetailData = scrapy.Field()

