import logging
import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors
from zcSpider.items import MatchDataItem
from zcSpider.items import OuOddsItem
from zcSpider.items import YaOddsItem
from zcSpider.items import YaOddsDetailItem
from zcSpider.items import SizeOddsItem
from zcSpider.items import SizeOddsDetailItem
from zcSpider.mySql.MySql import MySql


class MySqlPipeline(object):

    def __init__(self, db_pool):
        self.db_pool = db_pool

    @classmethod
    def from_settings(cls, settings):
        # db_params = dict(
        #     host=settings['MYMySql_HOST'],
        #     user=settings['MYMySql_USER'],
        #     password=settings['MYMySql_PASSWORD'],
        #     port=settings['MYMySql_PORT'],
        #     db=settings['MYMySql_DB'],
        #     charset="utf-8",
        #     use_unicode=True,
        #     cursorclass=cursors.Cursor
        # )
        # db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        db_pool = adbapi.ConnectionPool('pymysql',
                                        host=settings["MYSQL_HOST"],
                                        db=settings["MYSQL_DB"],
                                        user=settings["MYSQL_USER"],
                                        password=settings["MYSQL_PASSWORD"],
                                        charset="utf8",
                                        cursorclass=pymysql.cursors.DictCursor,
                                        use_unicode=True)
        return cls(db_pool)

    def process_item(self, item, spider):
        if isinstance(item, MatchDataItem):
            self.db_pool.runInteraction(self.process_match_item, item)
        elif isinstance(item, OuOddsItem):
            self.db_pool.runInteraction(self.process_ouodds_item, item)
        elif isinstance(item, YaOddsItem):
            self.db_pool.runInteraction(self.process_yaodds_item, item)
        elif isinstance(item, YaOddsDetailItem):
            self.db_pool.runInteraction(self.process_yaoddsdetail_item, item)
        elif isinstance(item, SizeOddsItem):
            self.db_pool.runInteraction(self.process_sizeodds_item, item)
        elif isinstance(item, SizeOddsDetailItem):
            self.db_pool.runInteraction(self.process_sizeoddsdetail_item, item)

    def process_match_item(self, cursor, item):
        try:
            #获取主队编号
            mmid = MySql.select_name(cursor, 'b_team', item['mmTeam'])
            if (mmid == 0):
                if MySql.addTeamItem(cursor, item['mmTeam'], '', ''):
                    mmid = MySql.select_name(cursor, 'b_team', item['mmTeam'])

            #获取客队球队编号
            mdid = MySql.select_name(cursor, 'b_team', item['mdTeam'])
            if (mdid == 0):
                if MySql.addTeamItem(cursor, item['mdTeam'], '', ''):
                    mdid = MySql.select_name(cursor, 'b_team', item['mdTeam'])

            #获取联赛编号
            mlsid = MySql.select_name(cursor, 'b_lmatch', item['mlsName'])
            if (mlsid == 0):
                if MySql.addlmMatchItem(cursor, item['mlsName'], '', ''):
                    mlsid = MySql.select_name(cursor, 'b_lmatch', item['mlsName'])

            #判断当前比赛是否已经记录
            mbId = MySql.getMatchId(cursor, item['mid'])
            if (mbId == 0):
                item['mmTeamId'] = mmid
                item['mdTeamId'] = mdid
                item['mlsId'] = mlsid
                if MySql.addMatchItem(cursor, item):
                    logging.warning('AddData[MatchDate]Mid[{0}]'.format(item['mid']))
        except Exception as e:
            logging.error('MatchDataPipeline Error: {0}'.format(e))

    def process_ouodds_item(self, cursor, item):
        try:
            #判断当前比赛是否已经记录
            mbId = MySql.getMatchId(cursor, item['mid'])
            if (mbId > 0):
                # 获取博彩公司编号
                #item['mlyName'] = 'Interwetten'
                mlyid = MySql.select_name(cursor, 'b_lottery', item['mlyName'])
                if (mlyid == 0):
                    if MySql.addLotteryItem(cursor, item['mlyName'], '', ''):
                        mlyid = MySql.select_name(cursor, 'b_lottery', item['mlyName'])
                item['mlyId'] = mlyid
                ooid = MySql.getOuOddsId(cursor, item['mid'], mlyid)
                if (ooid == 0) and (mlyid > 0):
                    if MySql.addOuOddsItem(cursor, item):
                        logging.warning('AddData[OuOdds]Mid[{0}][{1}]'.format(item['mid'], item['mlyName']))
        except Exception as e:
            logging.error('OuOddsDataPipeline Error: {0}'.format(e))

    def process_yaodds_item(self, cursor, item):
        try:
            #判断当前比赛是否已经记录
            mbId = MySql.getMatchId(cursor, item['mid'])
            if (mbId > 0):
                # 获取博彩公司编号
                mlyid = MySql.select_name(cursor, 'b_lottery', item['mlyName'])
                if (mlyid == 0):
                    if MySql.addLotteryItem(cursor, item['mlyName'], '', ''):
                        mlyid = MySql.select_name(cursor, 'b_lottery', item['mlyName'])
                item['mlyId'] = mlyid
                ooid = MySql.getYaOddsId(cursor, item['mid'], mlyid)
                if (ooid == 0) and (mlyid > 0):
                    if MySql.addYaOddsItem(cursor, item):
                        logging.warning('AddData[YaOdds]Mid[{0}][{1}]'.format(item['mid'], item['mlyName']))
        except Exception as e:
            logging.error('YaOddsDataPipeline Error: {0}'.format(e))

    def process_yaoddsdetail_item(self, cursor, item):
        try:
            # 获取博彩公司编号
            mlyid = MySql.select_name(cursor, 'b_lottery', item['mlyName'])
            # 获取亚赔ID
            myoid = MySql.getYaOddsId(cursor, item['mid'], mlyid)
            # 判断明细是否已经存在
            mdid = MySql.getYaDetailId(cursor, myoid, item['mDisc'])
            if (mdid == 0) and (myoid > 0):
                item['myoid'] = myoid
                MySql.addYaDetailItem(cursor, item)
        except Exception as e:
            logging.error('YaOddsDetailDataPipeline Error: {0}'.format(e))

    def process_sizeodds_item(self, cursor, item):
        try:
            #判断当前比赛是否已经记录
            mbId = MySql.getMatchId(cursor, item['mid'])
            if (mbId > 0):
                # 获取博彩公司编号
                mlyid = MySql.select_name(cursor, 'b_lottery', item['mlyName'])
                if (mlyid == 0):
                    if MySql.addLotteryItem(cursor, item['mlyName'], '', ''):
                        mlyid = MySql.select_name(cursor, 'b_lottery', item['mlyName'])
                item['mlyId'] = mlyid
                ooid = MySql.getSizeOddsId(cursor, item['mid'], mlyid)
                if (ooid == 0) and (mlyid > 0):
                    if MySql.addSizeOddsItem(cursor, item):
                        logging.warning('AddData[SizeOdds]Mid[{0}][{1}]'.format(item['mid'], item['mlyName']))
        except Exception as e:
            logging.error('SizeOddsDataPipeline Error: {0}'.format(e))

    def process_sizeoddsdetail_item(self, cursor, item):
        try:
            # 获取博彩公司编号
            mlyid = MySql.select_name(cursor, 'b_lottery', item['mlyName'])
            # 获取亚赔ID
            myoid = MySql.getSizeOddsId(cursor, item['mid'], mlyid)
            # 判断明细是否已经存在
            mdid = MySql.getSizeDetailId(cursor, myoid, item['mDisc'])
            if (mdid == 0) and (myoid > 0):
                item['msoid'] = myoid
                MySql.addSizeDetailItem(cursor, item)
        except Exception as e:
            logging.error('SizeOddsDetailDataPipeline Error: {0}'.format(e))
