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

## Requirements
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
Your files will be executed with MySQLdb version 2.0.x
Your files will be executed with SQLAlchemy version 1.4.x
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (`version 2.8.*`)
All your files must be executable
All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__))`
All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
You are not allowed to use `execute with sqlalchemy`

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

