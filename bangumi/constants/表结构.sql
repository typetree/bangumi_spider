/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.7.20-0ubuntu0.16.04.1 : Database - bangumi
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `spider_version` */

CREATE TABLE `spider_version` (
  `id` int(11) NOT NULL,
  `optimistic` int(11) NOT NULL,
  `version` varchar(32) NOT NULL COMMENT '版本',
  `spider_version` varchar(32) NOT NULL COMMENT '创建时间+版本',
  `active_degree` int(11) NOT NULL DEFAULT '50' COMMENT '爬虫活跃度',
  `log` varchar(100) DEFAULT NULL COMMENT '日志',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  KEY `spider_version` (`spider_version`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `user_friends` */

CREATE TABLE `user_friends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `optimistic` int(11) NOT NULL,
  `user_id` int(11) NOT NULL COMMENT '用户',
  `user_code` varchar(32) NOT NULL COMMENT '用户编码',
  `user_name` varchar(32) NOT NULL COMMENT '用户名',
  `friend_user_id` int(11) NOT NULL COMMENT '关注的好友',
  `friend_user_code` varchar(32) NOT NULL COMMENT '关注的好友编码',
  `friend_user_name` varchar(32) NOT NULL COMMENT '关注的好友名',
  `is_friend` varchar(32) DEFAULT NULL COMMENT '是否互相关注',
  `spider_version` varchar(32) NOT NULL COMMENT '更新版本：时间戳',
  `status` varchar(32) NOT NULL COMMENT 'ENABLE=可用,ENABLE=不可用',
  `create_time` datetime NOT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`,`user_code`,`friend_user_id`,`friend_user_code`,`spider_version`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `users_info` */

CREATE TABLE `users_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `optimistic` int(11) NOT NULL,
  `code` varchar(32) NOT NULL COMMENT '用户编码',
  `name` varchar(32) NOT NULL COMMENT '用户名',
  `join_time` varchar(32) DEFAULT NULL COMMENT '注册时间',
  `homepage` varchar(256) NOT NULL COMMENT '用户主页',
  `bangumi_user_id` varchar(32) DEFAULT NULL COMMENT 'bgm的id',
  `status` varchar(32) NOT NULL COMMENT '状态 ENABLE=可用,ENABLE=不可用',
  `hash_value` varchar(50) DEFAULT NULL COMMENT '更新对比值',
  `spider_version` varchar(32) DEFAULT NULL COMMENT '更新版本：时间戳',
  `active_degree` int(11) NOT NULL DEFAULT '100' COMMENT '活跃度',
  `friends_num` int(11) DEFAULT NULL COMMENT '好友数',
  `last_active_time` datetime DEFAULT NULL COMMENT '最后一次活跃时间',
  `intro` varchar(1000) DEFAULT NULL COMMENT '自我介绍',
  `anime_do` int(11) DEFAULT NULL COMMENT '动画在看',
  `anime_collect` int(11) DEFAULT NULL COMMENT '动画已看',
  `anime_wish` int(11) DEFAULT NULL COMMENT '动画想看',
  `anime_on_hold` int(11) DEFAULT NULL COMMENT '动画搁置',
  `anime_dropped` int(11) DEFAULT NULL COMMENT '动画抛弃',
  `game_do` int(11) DEFAULT NULL COMMENT '游戏在看',
  `game_collect` int(11) DEFAULT NULL COMMENT '游戏已看',
  `game_wish` int(11) DEFAULT NULL COMMENT '游戏想看',
  `game_on_hold` int(11) DEFAULT NULL COMMENT '游戏搁置',
  `game_dropped` int(11) DEFAULT NULL COMMENT '游戏抛弃',
  `book_do` int(11) DEFAULT NULL COMMENT '图书在看',
  `book_collect` int(11) DEFAULT NULL COMMENT '图书已看',
  `book_wish` int(11) DEFAULT NULL COMMENT '图书想看',
  `book_on_hold` int(11) DEFAULT NULL COMMENT '图书搁置',
  `book_dropped` int(11) DEFAULT NULL COMMENT '图书抛弃',
  `real_do` int(11) DEFAULT NULL COMMENT '电视剧在看',
  `real_collect` int(11) DEFAULT NULL COMMENT '电视剧已看',
  `real_wish` int(11) DEFAULT NULL COMMENT '电视剧想看',
  `real_on_hold` int(11) DEFAULT NULL COMMENT '电视剧搁置',
  `real_dropped` int(11) DEFAULT NULL COMMENT '电视剧抛弃',
  `group_num` int(11) DEFAULT NULL COMMENT '小组数',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  KEY `code` (`code`,`bangumi_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
