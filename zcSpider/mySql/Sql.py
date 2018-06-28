import mysql.connector

from zcSpider import settings
from zcSpider.items import MatchDataItem

MYSQL_HOST = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, database=MYSQL_DB)
cur = cnx.cursor(buffered=True)


class Sql:
    @classmethod
    def addTeamItem(cls, name, fullname, remark):
        try:
            sql = 'INSERT INTO b_team(`name`, `fullname`, `remark`) VALUES(%(name)s, %(fullname)s, %(remark)s)'
            values = {
                'name': name,
                'fullname': fullname,
                'remark': remark
            }
            cur.execute(sql, values)
            cnx.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def addlmMatchItem(cls, name, fullname, remark):
        try:
            sql = 'INSERT INTO b_lmatch(`name`, `fullname`, `remark`) VALUES(%(name)s, %(fullname)s, %(remark)s)'
            values = {
                'name': name,
                'fullname': fullname,
                'remark': remark
            }
            cur.execute(sql, values)
            cnx.commit()
            return True
        except:
            return False

    @classmethod
    def addLotteryItem(cls, name, fullname, remark):
        try:
            sql = 'INSERT INTO b_lottery(`name`, `fullname`, `remark`) VALUES(%(name)s, %(fullname)s, %(remark)s)'
            values = {
                'name': name,
                'fullname': fullname,
                'remark': remark
            }
            cur.execute(sql, values)
            cnx.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def addMatchItem(cls, item):
        try:
            if isinstance(item, MatchDataItem):
                sql = 'INSERT INTO matchdata(`mid`, `mlsid`, `mteamid`, `dteamid`, `isend`, `rq`, `jq`, `sq`, `status`, `rstatus`, ' \
                      '`week`, `mdate`, `mtime`, `sdate`) VALUES(%(mid)s, %(mlsid)s, %(mteamid)s, %(dteamid)s, %(isend)s, %(rq)s, %(jq)s' \
                      ', %(sq)s, %(status)s, %(rstatus)s, %(week)s, %(mdate)s, %(mtime)s, %(sdate)s)'
                values = {
                    'mid': item['mid'],
                    'mlsid': item['mlsId'],
                    'mteamid': item['mmTeamId'],
                    'dteamid': item['mdTeamId'],
                    'isend': item['mIsend'],
                    'rq': item['mQr'],
                    'jq': item['mQj'],
                    'sq': item['mQs'],
                    'status': item['mWinStatus'],
                    'rstatus': item['mRWinStatus'],
                    'week': item['mWeek'].encode('utf-8'),
                    'mdate': item['mDate'].encode('utf-8'),
                    'mtime': item['mTime'].encode('utf-8'),
                    'sdate': item['mSell'].encode('utf-8')
                }
                cur.execute(sql, values)
                cnx.commit()
                return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def addOuOddsItem(cls, item):
        try:
            sql = 'INSERT INTO ouodds(`mid`, `lyid`, `odds11`, `odds12`, `odds13`, `odds21`, `odds22`, `odds23`, `chance11`, `chance12`, ' \
                  '`chance13`, `chance21`, `chance22`, `chance23`, `retratio1`, `retratio2`, `kaili11`, `kaili12`, `kaili13`, `kaili21`, `kaili22`, `kaili23`) ' \
                  'VALUES(%(mid)s, %(lyid)s, %(odds11)s, %(odds12)s, %(odds13)s, %(odds21)s, %(odds22)s, %(odds23)s, %(chance11)s, %(chance12)s' \
                  ', %(chance13)s, %(chance21)s, %(chance22)s, %(chance23)s, %(retratio1)s, %(retratio2)s, %(kaili11)s, %(kaili12)s, %(kaili13)s, %(kaili21)s, %(kaili22)s, %(kaili23)s)'
            values = {
                'mid': item['mid'],
                'lyid': item['mlyId'],
                'odds11': item['mOdds11'],
                'odds12': item['mOdds12'],
                'odds13': item['mOdds13'],
                'odds21': item['mOdds21'],
                'odds22': item['mOdds22'],
                'odds23': item['mOdds23'],
                'chance11': item['mChance11'],
                'chance12': item['mChance12'],
                'chance13': item['mChance13'],
                'chance21': item['mChance21'],
                'chance22': item['mChance22'],
                'chance23': item['mChance23'],
                'retratio1': item['mRetRatio1'],
                'retratio2': item['mRetRatio2'],
                'kaili11': item['mKaili11'],
                'kaili12': item['mKaili12'],
                'kaili13': item['mKaili13'],
                'kaili21': item['mKaili21'],
                'kaili22': item['mKaili22'],
                'kaili23': item['mKaili23']
            }
            cur.execute(sql, values)
            cnx.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def addYaOddsItem(cls, item):
        try:
            sql = 'INSERT INTO yaodds(`mid`, `lyid`, `immodds1`, `immdisc`, `immodds2`, `immdate`, `immstatus`, ' \
                  '`initodds1`, `initdisc`, `initodds2`, `initdate`, `myid`, `dtdate`) VALUES(%(mid)s, %(lyid)s, %(immodds1)s, ' \
                  '%(immdisc)s, %(immodds2)s, %(immdate)s, %(immstatus)s, %(initodds1)s, %(initdisc)s, ' \
                  '%(initodds2)s, %(initdate)s, %(myid)s, %(dtdate)s)'
            values = {
                'mid': item['mid'],
                'lyid': item['mlyId'],
                'immodds1': item['mImmOdds1'],
                'immdisc': item['mImmDisc'],
                'immodds2': item['mImmOdds2'],
                'immdate': item['mImmDate'],
                'immstatus': item['mImmStatus'],
                'initodds1': item['mInitOdds1'],
                'initdisc': item['mInitDisc'],
                'initodds2': item['mInitOdds2'],
                'initdate': item['mInitDate'],
                'myid': item['mmyId'],
                'dtdate': item['mDtDate']
            }
            cur.execute(sql, values)
            cnx.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def addSizeOddsItem(cls, item):
        try:
            sql = 'INSERT INTO sizeodds(`mid`, `lyid`, `immodds1`, `immdisc`, `immodds2`, `immdate`, `immstatus`, ' \
                  '`initodds1`, `initdisc`, `initodds2`, `initdate`, `myid`, `dtdate`) VALUES(%(mid)s, %(lyid)s, %(immodds1)s, ' \
                  '%(immdisc)s, %(immodds2)s, %(immdate)s, %(immstatus)s, %(initodds1)s, %(initdisc)s, ' \
                  '%(initodds2)s, %(initdate)s, %(myid)s, %(dtdate)s)'
            values = {
                'mid': item['mid'],
                'lyid': item['mlyId'],
                'immodds1': item['mImmOdds1'],
                'immdisc': item['mImmDisc'],
                'immodds2': item['mImmOdds2'],
                'immdate': item['mImmDate'],
                'immstatus': item['mImmStatus'],
                'initodds1': item['mInitOdds1'],
                'initdisc': item['mInitDisc'],
                'initodds2': item['mInitOdds2'],
                'initdate': item['mInitDate'],
                'myid': item['mmyId'],
                'dtdate': item['mDtDate']
            }
            cur.execute(sql, values)
            cnx.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def addYaDetailItem(cls, item):
        try:
            sql = 'INSERT INTO yaoddsdetail(`yoid`, `disc`, `odds1`, `odds2`) VALUES(%(yoid)s, %(disc)s, %(odds1)s, %(odds2)s)'
            values = {
                'yoid': item['myoid'],
                'disc': item['mDisc'],
                'odds1': item['mOdds1'],
                'odds2': item['mOdds2']
            }
            cur.execute(sql, values)
            cnx.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def addSizeDetailItem(cls, item):
        try:
            sql = 'INSERT INTO sizeoddsdetail(`soid`, `disc`, `odds1`, `odds2`) VALUES(%(soid)s, %(disc)s, %(odds1)s, %(odds2)s)'
            values = {
                'soid': item['msoid'],
                'disc': item['mDisc'],
                'odds1': item['mOdds1'],
                'odds2': item['mOdds2']
            }
            cur.execute(sql, values)
            cnx.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def getOuOddsId(cls, mid, lyid):
        sql = 'SELECT id FROM ouodds WHERE mid=%(mid)s and lyid=%(lyid)s'
        value = {
            'mid': mid,
            'lyid': lyid
        }

        cur.execute(sql, value)
        datas = cur.fetchall()
        if len(datas) > 0:
            return datas[0][0]
        else:
            return 0

    @classmethod
    def getYaOddsId(cls, mid, lyid):
        sql = 'SELECT id FROM yaodds WHERE mid=%(mid)s and lyid=%(lyid)s'
        value = {
            'mid': mid,
            'lyid': lyid
        }

        cur.execute(sql, value)
        datas = cur.fetchall()
        if len(datas) > 0:
            return datas[0][0]
        else:
            return 0

    @classmethod
    def getSizeOddsId(cls, mid, lyid):
        sql = 'SELECT id FROM sizeodds WHERE mid=%(mid)s and lyid=%(lyid)s'
        value = {
            'mid': mid,
            'lyid': lyid
        }

        cur.execute(sql, value)
        datas = cur.fetchall()
        if len(datas) > 0:
            return datas[0][0]
        else:
            return 0

    @classmethod
    def getYaDetailId(cls, myoid, mdisc):
        sql = 'SELECT id FROM yaoddsdetail WHERE yoid=%(yoid)s and disc=%(disc)s'
        value = {
            'yoid': myoid,
            'disc': mdisc
        }

        cur.execute(sql, value)
        datas = cur.fetchall()
        if len(datas) > 0:
            return datas[0][0]
        else:
            return 0

    @classmethod
    def getSizeDetailId(cls, msoid, mdisc):
        sql = 'SELECT id FROM sizeoddsdetail WHERE soid=%(soid)s and disc=%(disc)s'
        value = {
            'soid': msoid,
            'disc': mdisc
        }

        cur.execute(sql, value)
        datas = cur.fetchall()
        if len(datas) > 0:
            return datas[0][0]
        else:
            return 0

    @classmethod
    def getMatchId(cls, mid):
        sql = 'SELECT id FROM matchdata WHERE mid=%(mid)s'
        value = {
            'mid': mid
        }

        cur.execute(sql, value)
        datas = cur.fetchall()
        if len(datas) > 0:
            return datas[0][0]
        else:
            return 0


    @classmethod
    def select_name(cls, tablename, name):
        sql = 'SELECT id FROM ' + tablename + ' WHERE name=%(name)s'
        value = {
            'name': name
        }

        cur.execute(sql, value)
        datas = cur.fetchall()
        if len(datas) > 0:
            return datas[0][0]
        else:
            return 0


if __name__ == '__main__':
    vue = Sql.select_name('b_team', '悉尼FC')
    print(vue)
