"""
This script creates a photon_testbeds table in the 'Inventory'
database on phpMyAdmin at 10.21.1.181 at work
code help from https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
"""

from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'Inventory'

TABLES = {}     #dictionary of potential db tables

TABLES['photon_testbeds'] = (
    "CREATE TABLE `photon_testbeds` ("
    "  `indx_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tb_name` varchar(14) NOT NULL,"
    "  `device` varchar(16) NOT NULL,"
    "  `part_no` varchar(16) NOT NULL,"
    "  `serial_no` varchar(16) NOT NULL,"
    "  `ip_addr` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`indx_no`)"
    ") ENGINE=InnoDB")

cnx = mysql.connector.connect(user='bbdlc', password='bbdlc',
                              host='10.21.1.181',
                              database='Inventory')
cursor = cnx.cursor()

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()