

create table if not exists tb_pc28(
id int primary key auto_increment,
r_id  int unique not null ,
r_date datetime not null,
r_value  int  not null 
);

create index ind_pc28 on tb_pc28(r_id,r_date);


create table if not exists tb_crazy28(
id int primary key auto_increment,
r_id  int unique not null ,
r_date datetime not null,
r_value  int  not null 
);

create index ind_crazy28 on tb_crazy28(r_id,r_date);

create table if not exists tb_korea28(
id int primary key auto_increment,
r_id  int unique not null ,
r_date datetime not null,
r_value  int  not null 
);

create index ind_korea28 on tb_korea28(r_id,r_date);


create table if not exists tb_speed16(
id int primary key auto_increment,
r_id  int unique not null ,
r_date datetime not null,
r_value  int  not null 
);

create index ind_speed16 on tb_speed16(r_id,r_date);