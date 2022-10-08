# 0x0F. Python - Object-relational mapping


## Objectives
+ How to connect to a MySQL database from a Python script
+ How to SELECT rows in a MySQL table from a Python script
+ How to INSERT rows in a MySQL table from a Python script
+ What ORM means
+ How to map a Python Class to a MySQL table

## Background Context
In this project, we will link two amazing worlds: Databases and Python!
In the first part, we will use the module MySQLdb to connect to a MySQL database and execute SQL queries.
In the second part, we will use the module SQLAlchemy an Object Relational Mapper (ORM).
The biggest difference is: no more SQL queries!

## More Info
### Install MySQLdb module version 2.0.x
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)

### Install `SQLAlchemy` module `version 1.4.x`
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'

