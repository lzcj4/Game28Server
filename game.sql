
DROP TABLE IF EXISTS `tb_crazy28`;
CREATE TABLE `tb_crazy28` (
  `id` int(11) NOT NULL auto_increment,
  `r_id` int(11) NOT NULL,
  `r_date` datetime NOT NULL,
  `r_value` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `ind_crazy28` (`r_id`,`r_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_korea28`;
CREATE TABLE `tb_korea28` (
  `id` int(11) NOT NULL auto_increment,
  `r_id` int(11) NOT NULL,
  `r_date` datetime NOT NULL,
  `r_value` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `ind_korea28` (`r_id`,`r_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_pc28`;
CREATE TABLE `tb_pc28` (
  `id` int(11) NOT NULL auto_increment,
  `r_id` int(11) NOT NULL,
  `r_date` datetime NOT NULL,
  `r_value` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `ind_pc28` (`r_id`,`r_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_speed16`;
CREATE TABLE `tb_speed16` (
  `id` int(11) NOT NULL auto_increment,
  `r_id` int(11) NOT NULL,
  `r_date` datetime NOT NULL,
  `r_value` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `ind_speed16` (`r_id`,`r_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

