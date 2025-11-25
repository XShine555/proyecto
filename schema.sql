CREATE DATABASE IF NOT EXISTS `proyecto`;
USE `proyecto`;

CREATE TABLE IF NOT EXISTS `USUARIS` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cognoms` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tipus` enum('alumne','professor','admin') NOT NULL,
  `targeta_rfid` varchar(50) DEFAULT NULL,
  `actiu` tinyint(1) DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `targeta_rfid` (`targeta_rfid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `CLASSES` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `planta` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `ASSIGNATURES` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `classe_id` int NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `ASSIGNATURES_ibfk_1` FOREIGN KEY (`classe_id`) REFERENCES `CLASSES` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `DISPOSITIUS` (
  `id` int NOT NULL AUTO_INCREMENT,
  `device_id` varchar(50) NOT NULL,
  `actiu` tinyint(1) DEFAULT '1',
  `classe_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `device_id` (`device_id`),
  KEY `DISPOSITIUS_CLASSEID` (`classe_id`),
  CONSTRAINT `DISPOSITIUS_CLASSEID` FOREIGN KEY (`classe_id`) REFERENCES `CLASSES` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `ALERTES` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuari_id` int NOT NULL,
  `tipus` varchar(50) NOT NULL,
  `percentatge_faltes` decimal(5,2) DEFAULT NULL,
  `notificat` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `usuari_id` (`usuari_id`),
  CONSTRAINT `ALERTES_ibfk_1` FOREIGN KEY (`usuari_id`) REFERENCES `USUARIS` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `HORARIS` (
  `id` int NOT NULL AUTO_INCREMENT,
  `timestamp_inici` datetime NOT NULL,
  `timestamp_fi` datetime NOT NULL,
  `assignatura_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `assignatura_id` (`assignatura_id`),
  CONSTRAINT `HORARIS_ibfk_1` FOREIGN KEY (`assignatura_id`) REFERENCES `ASSIGNATURES` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `ASSISTENCIA` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuari_id` int NOT NULL,
  `assignatura_id` int NOT NULL,
  `horari_id` int NOT NULL,
  `timestamp` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `tipus_registre` enum('assistit','retard','no_assistit') NOT NULL,
  PRIMARY KEY (`id`, `usuari_id`, `assignatura_id`, `horari_id`),
  CONSTRAINT `ASSISTENCIA_ibfk_1` FOREIGN KEY (`usuari_id`) REFERENCES `USUARIS` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ASSISTENCIA_ibfk_2` FOREIGN KEY (`assignatura_id`) REFERENCES `ASSIGNATURES` (`id`) ON DELETE CASCADE,
  CONSTRAINT `ASSISTENCIA_ibfk_3` FOREIGN KEY (`horari_id`) REFERENCES `HORARIS` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `JUSTIFICACIONS` (
  `id` int NOT NULL AUTO_INCREMENT,
  `assistencia_id` int NOT NULL,
  `motiu` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `document` varchar(255) DEFAULT NULL,
  `estat` enum('pendiente','aprobado','rechazado') DEFAULT 'pendiente',
  `data_solicitud` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `assistencia_id` (`assistencia_id`),
  CONSTRAINT `JUSTIFICACIONS_ibfk_1` FOREIGN KEY (`assistencia_id`) REFERENCES `ASSISTENCIA` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `USUARIS_ASSIGNATURES` (
  `usuari_id` int NOT NULL,
  `assignatura_id` int NOT NULL,
  PRIMARY KEY (`usuari_id`,`assignatura_id`),
  KEY `assignatura_id` (`assignatura_id`),
  CONSTRAINT `USUARIS_ASSIGNATURES_ibfk_1` FOREIGN KEY (`usuari_id`) REFERENCES `USUARIS` (`id`) ON DELETE CASCADE,
  CONSTRAINT `USUARIS_ASSIGNATURES_ibfk_2` FOREIGN KEY (`assignatura_id`) REFERENCES `ASSIGNATURES` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;