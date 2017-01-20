-- MySQL dump 10.11
--
-- Host: localhost    Database: game
-- ------------------------------------------------------
-- Server version	5.0.41-community-nt

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
-- Table structure for table `tb_crazy28`
--

DROP TABLE IF EXISTS `tb_crazy28`;
CREATE TABLE `tb_crazy28` (
  `id` int(11) NOT NULL auto_increment,
  `r_id` int(11) NOT NULL,
  `r_date` datetime NOT NULL,
  `r_value` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `ind_crazy28` (`r_id`,`r_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_crazy28`
--

LOCK TABLES `tb_crazy28` WRITE;
/*!40000 ALTER TABLE `tb_crazy28` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_crazy28` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_korea28`
--

DROP TABLE IF EXISTS `tb_korea28`;
CREATE TABLE `tb_korea28` (
  `id` int(11) NOT NULL auto_increment,
  `r_id` int(11) NOT NULL,
  `r_date` datetime NOT NULL,
  `r_value` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `ind_korea28` (`r_id`,`r_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_korea28`
--

LOCK TABLES `tb_korea28` WRITE;
/*!40000 ALTER TABLE `tb_korea28` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_korea28` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_pc28`
--

DROP TABLE IF EXISTS `tb_pc28`;
CREATE TABLE `tb_pc28` (
  `id` int(11) NOT NULL auto_increment,
  `r_id` int(11) NOT NULL,
  `r_date` datetime NOT NULL,
  `r_value` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `ind_pc28` (`r_id`,`r_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_pc28`
--

LOCK TABLES `tb_pc28` WRITE;
/*!40000 ALTER TABLE `tb_pc28` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_pc28` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_speed16`
--

DROP TABLE IF EXISTS `tb_speed16`;
CREATE TABLE `tb_speed16` (
  `id` int(11) NOT NULL auto_increment,
  `r_id` int(11) NOT NULL,
  `r_date` datetime NOT NULL,
  `r_value` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `ind_speed16` (`r_id`,`r_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `tb_speed16`
--

LOCK TABLES `tb_speed16` WRITE;
/*!40000 ALTER TABLE `tb_speed16` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_speed16` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-20  2:26:54
