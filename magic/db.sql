-- MariaDB dump 10.19  Distrib 10.5.19-MariaDB, for debian-linux-gnu (aarch64)
--
-- Host: localhost    Database: magic8ball
-- ------------------------------------------------------
-- Server version	10.5.19-MariaDB-0+deb11u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer` (
  `id` int(11) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `emoji` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (0,'It is certain','V.py'),(1,'It is decidedly so.','V.py'),(2,'Without a doubt.','V.py'),(3,'Yes, definitely.','V.py'),(4,'You may rely on it.','V.py'),(5,'As I see it, yes.','V.py'),(6,'Most likely.','V.py'),(7,'Outlook good.','V.py'),(8,'Yes.','V.py'),(9,'Signs point to yes.','V.py'),(10,'Reply hazy, try again.','smileybigeyes.py'),(11,'Ask again later.','smileybigeyes.py'),(12,'Better not tell you now.','smileybigeyes.py'),(13,'Cannot predict now.','smileybigeyes.py'),(14,'Concentrate and ask again.','smileybigeyes.py'),(15,'Don\'t count on it.','X.py'),(16,'My reply is no.','X.py'),(17,'My sources say no.','X.py'),(18,'Outlook not so good.','sadbigeyes.py'),(19,'Very doubtful.','sadbigeyes.py');
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-22 10:55:31
