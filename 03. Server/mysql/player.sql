-- Offline Shop System - player veritabani
-- item.window enum'una IKASHOP_OFFLINESHOP, IKASHOP_SAFEBOX, IKASHOP_AUCTION eklenir.
-- Sira, client ve game tarafindaki window enum sirasiyla ayni olmali (kendi enum'unu kontrol et).

ALTER TABLE `item` MODIFY COLUMN `window` ENUM('INVENTORY','EQUIPMENT','SAFEBOX','MALL','DRAGON_SOUL_INVENTORY','BELT_INVENTORY','GROUND','IKASHOP_OFFLINESHOP','IKASHOP_SAFEBOX','IKASHOP_AUCTION') NOT NULL;
ALTER TABLE `item` ADD COLUMN `ikashop_data` TINYTEXT NULL DEFAULT NULL;

CREATE TABLE IF NOT EXISTS `ikashop_auction_offer` (
  `seller` int(10) unsigned NOT NULL,
  `buyer` int(10) unsigned NOT NULL,
  `buyer_name` varchar(30) NOT NULL,
  `price` bigint(20) unsigned NOT NULL,
  `datetime` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `seen` tinyint(3) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`seller`,`buyer`,`price`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
CREATE TABLE IF NOT EXISTS `ikashop_notification` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `owner` int(10) unsigned NOT NULL,
  `type` int(10) unsigned NOT NULL,
  `who` varchar(50) NOT NULL,
  `what` int(10) unsigned NOT NULL,
  `format` varchar(50) NOT NULL,
  `seen` tinyint(4) NOT NULL DEFAULT 0,
  `datetime` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
CREATE TABLE IF NOT EXISTS `ikashop_offlineshop` (
  `owner` int(10) unsigned NOT NULL,
  `duration` int(10) unsigned NOT NULL DEFAULT 0,
  `map` int(10) unsigned NOT NULL DEFAULT 0,
  `x` int(10) unsigned NOT NULL DEFAULT 0,
  `y` int(10) unsigned NOT NULL DEFAULT 0,
  `decoration` int(10) unsigned NOT NULL DEFAULT 0,
  `decoration_time` int(10) unsigned NOT NULL DEFAULT 0,
  `lock_index` int(10) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`owner`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
CREATE TABLE IF NOT EXISTS `ikashop_private_offer` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `seller` int(10) unsigned NOT NULL,
  `buyer` int(10) unsigned NOT NULL,
  `item` int(10) unsigned NOT NULL,
  `price` bigint(20) unsigned NOT NULL,
  `notified` tinyint(3) unsigned NOT NULL,
  `accepted` tinyint(3) unsigned NOT NULL,
  `buyer_name` varchar(30) NOT NULL,
  `datetime` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
CREATE TABLE IF NOT EXISTS `ikashop_safebox` (
  `owner` int(10) unsigned NOT NULL,
  `gold` bigint(20) unsigned NOT NULL,
  `cheque` int(10) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`owner`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
CREATE TABLE IF NOT EXISTS `ikashop_sale` (
  `id` int(10) unsigned NOT NULL,
  `vnum` int(10) unsigned NOT NULL,
  `count` int(10) unsigned NOT NULL,
  `price` bigint(20) unsigned NOT NULL,
  `datetime` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
