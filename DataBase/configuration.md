create user 'startover'@'%' identified  by 'startover';


权限
https://www.cnblogs.com/anzerong2012/p/10738186.html
grant all privileges on *.* to startover@'%' identified by 'startover';
flush privileges;

create database gameserver;

端口修改
https://blog.csdn.net/shardy0/article/details/87912345


允许外网访问
https://www.cnblogs.com/zou-zou/p/9661422.html
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
注释掉bind-address = 127.0.0.1：
重启sudo service mysql restart


create database 'gameserver' default character set utf8 collate utf8_general_ci;

