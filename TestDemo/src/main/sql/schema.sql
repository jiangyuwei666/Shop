CREATE TABLE book (
bid BIGINT ( 20 ) NOT NULL AUTO_INCREMENT COMMENT '图书ID',
NAME VARCHAR ( 100 ) NOT NULL COMMENT '图书名称',
number INT ( 11 ) NOT NULL COMMENT '馆藏数量',
PRIMARY KEY ( bid ) 
)ENGINE =InnoDB AUTO_INCREMENT=1000 default charset=utf8 COMMENT ='图书表';

insert into book (bid, name, number)
values
    (1000, 'Java程序设计', 10),
    (1001, '数据结构', 10),
    (1002, '设计模式', 10),
    (1003, '编译原理', 10);


create table appointment(
bid bigint(20) not null comment '图书ID',
sid bigint(20) not null comment '学号',
appoint_time timestamp not null default current_timestamp on update current_timestamp comment '预约时间',
primary key (bid, sid),
index idx_appoint_time (appoint_time)
)engine=InnoDB default charset=utf8 comment='预约图书表';