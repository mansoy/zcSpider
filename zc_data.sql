-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: zc_data
-- ------------------------------------------------------
-- Server version	5.7.22-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `b_lmatch`
--

DROP TABLE IF EXISTS `b_lmatch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b_lmatch` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  `name` varchar(50) NOT NULL COMMENT '简称',
  `fullname` varchar(100) DEFAULT NULL COMMENT '全称',
  `remark` varchar(200) DEFAULT NULL COMMENT '描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `b_lottery`
--

DROP TABLE IF EXISTS `b_lottery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b_lottery` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `b_team`
--

DROP TABLE IF EXISTS `b_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b_team` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `b_website`
--

DROP TABLE IF EXISTS `b_website`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b_website` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT '',
  `desc` varchar(255) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `matchdata`
--

DROP TABLE IF EXISTS `matchdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `matchdata` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `mid` varchar(10) NOT NULL COMMENT '比赛场次编号',
  `mlmid` int(11) NOT NULL DEFAULT '0' COMMENT '赛事名称',
  `mteamid` int(11) NOT NULL COMMENT '主队Id',
  `dteamid` int(11) NOT NULL COMMENT '主队Id',
  `isend` int(10) NOT NULL DEFAULT '1' COMMENT '比赛状态, 1完成, 0未完成',
  `rq` int(11) NOT NULL DEFAULT '0' COMMENT '让球',
  `jq` int(11) NOT NULL DEFAULT '0' COMMENT '进球',
  `sq` int(11) NOT NULL DEFAULT '0' COMMENT '输球',
  `status` int(11) DEFAULT NULL COMMENT '比赛胜负情况',
  `rstatus` int(11) DEFAULT NULL COMMENT '让球胜负情况',
  `week` varchar(20) DEFAULT NULL COMMENT '比赛星期换算',
  `mdate` varchar(20) DEFAULT NULL COMMENT '比赛日期',
  `mtime` varchar(20) DEFAULT '' COMMENT '比赛时间',
  `sdate` varchar(20) DEFAULT NULL COMMENT '彩票截至日期',
  PRIMARY KEY (`id`),
  UNIQUE KEY `mid` (`mid`),
  KEY `index3` (`mdate`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ouodds`
--

DROP TABLE IF EXISTS `ouodds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ouodds` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `mid` varchar(10) NOT NULL COMMENT '比赛场次',
  `lyid` int(11) NOT NULL COMMENT '博彩公司编号',
  `odds11` float DEFAULT NULL COMMENT '即时欧赔_初_胜',
  `odds12` float DEFAULT NULL COMMENT '即时欧赔_初_平',
  `odds13` float DEFAULT '0' COMMENT '即时欧赔_初_负',
  `odds21` float DEFAULT NULL COMMENT '即时欧赔_终_胜',
  `odds22` float DEFAULT NULL COMMENT '即时欧赔_终_平',
  `odds23` float DEFAULT NULL COMMENT '即时欧赔_终_负',
  `chance11` float DEFAULT NULL COMMENT '即时概率_初_胜',
  `chance12` float DEFAULT NULL COMMENT '即时概率_初_平',
  `chance13` float DEFAULT NULL COMMENT '即时概率_初_负',
  `chance21` float DEFAULT NULL COMMENT '即时概率_终_胜',
  `chance22` float DEFAULT NULL COMMENT '即时概率_终_平',
  `chance23` float DEFAULT NULL COMMENT '即时概率_终_负',
  `retratio1` float DEFAULT NULL COMMENT '返还率_初',
  `retratio2` float DEFAULT NULL COMMENT '返还率_终',
  `kaili11` float DEFAULT NULL COMMENT '即时凯利_初_胜',
  `kaili12` float DEFAULT NULL COMMENT '即时凯利_初_平',
  `kaili13` float DEFAULT NULL COMMENT '即时凯利_初_负',
  `kaili21` float DEFAULT NULL COMMENT '即时凯利_终_胜',
  `kaili22` float DEFAULT NULL COMMENT '即时凯利_终_平',
  `kaili23` float DEFAULT NULL COMMENT '即时凯利_终_负',
  PRIMARY KEY (`id`),
  UNIQUE KEY `mid` (`mid`,`lyid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sizeodds`
--

DROP TABLE IF EXISTS `sizeodds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sizeodds` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `mid` varchar(10) NOT NULL DEFAULT '',
  `lyid` int(11) NOT NULL,
  `myid` varchar(20) DEFAULT '' COMMENT '大小指数编号(一场球赛一个博彩公司)',
  `dtdate` varchar(20) DEFAULT '' COMMENT '通过这个时间和myid可以获取明细数据',
  `immodds1` float DEFAULT NULL COMMENT '即时大小_大',
  `immdisc` varchar(50) DEFAULT '' COMMENT '即时盘口',
  `immodds2` float DEFAULT NULL COMMENT '即时大小_小',
  `immdate` varchar(20) DEFAULT '' COMMENT '变更时间',
  `immstatus` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1表示Odds1赢,2表示Odds1平',
  `initodds1` float DEFAULT NULL COMMENT '初始大小_大',
  `initdisc` varchar(50) DEFAULT '' COMMENT '初始盘口',
  `initodds2` float DEFAULT NULL COMMENT '初始大小_小',
  `initdate` varchar(20) DEFAULT '' COMMENT '变更时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `mid` (`mid`,`lyid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sizeoddsdetail`
--

DROP TABLE IF EXISTS `sizeoddsdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sizeoddsdetail` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `soid` bigint(20) NOT NULL,
  `odds1` float DEFAULT NULL,
  `disc` varchar(50) DEFAULT NULL,
  `odds2` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index2` (`soid`,`disc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `yaodds`
--

DROP TABLE IF EXISTS `yaodds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yaodds` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `mid` varchar(10) NOT NULL DEFAULT '',
  `lyid` int(11) NOT NULL,
  `myid` varchar(20) DEFAULT '' COMMENT '亚赔编号(一场球赛一个博彩公司)',
  `dtdate` varchar(20) DEFAULT '' COMMENT '通过这个时间和myid可以获取明细数据',
  `immodds1` float DEFAULT NULL COMMENT '即时盘口水1',
  `immdisc` varchar(50) DEFAULT '' COMMENT '即时盘口',
  `immodds2` float DEFAULT NULL COMMENT '即时盘口水2',
  `immdate` varchar(20) DEFAULT '' COMMENT '变更时间',
  `immstatus` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1表示Odds1赢,2表示Odds1平',
  `initodds1` float DEFAULT NULL COMMENT '初始盘口水1',
  `initdisc` varchar(50) DEFAULT '' COMMENT '初始盘口',
  `initodds2` float DEFAULT NULL COMMENT '初始盘口水2',
  `initdate` varchar(20) DEFAULT '' COMMENT '变更时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `mid` (`mid`,`lyid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `yaoddsdetail`
--

DROP TABLE IF EXISTS `yaoddsdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yaoddsdetail` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `yoid` bigint(20) NOT NULL,
  `odds1` float DEFAULT NULL,
  `disc` varchar(50) DEFAULT NULL,
  `odds2` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index2` (`yoid`,`disc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'zc_data'
--

--
-- Dumping routines for database 'zc_data'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-31 16:55:10
