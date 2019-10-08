"""
This script adds entries to the photon_testbeds table in the 'Inventory' database.
database on phpMyAdmin at 10.21.1.181 at work.
https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
"""

from __future__ import print_function
import mysql.connector

#connect to the database and store connecting into 'cnx'
cnx = mysql.connector.connect(user='bbdlc', password='bbdlc',
                              host='10.21.1.181',
                              database='Inventory')

#create a new cursor, by default a MySQLCursor object, using the connection's cursor() method
cursor = cnx.cursor()

# The information of the new employee is stored in the tuple data_employee.
add_tb_entry = ("INSERT INTO photon_testbeds "
               "(tb_name, device, part_no, serial_no, ip_addr) "
               "VALUES (%s, %s, %s, %s, %s)")

#dummy info to test insterting testbed information
for testbed in ('MCI-1', 'MCI-2', 'MCI-3', 'MCI-4'):
    data_tb_entry = (testbed, 'OLT-1', '1187xxxx', 'ADTN12345678', '10.13.245.321')
    #TODO: add code to parse the photon topology.xml files to get the necessary
    # testbed data for entry into the database.
    # parse for each device in the topology.xml then log entry.

    # Insert new testbed entry
    #The query to insert the new employee is executed and we
    cursor.execute(add_tb_entry, data_tb_entry)

    #retrieve the newly inserted value for the indx_no column
    # (an AUTO_INCREMENT column) using the lastrowid property of the cursor object.
    indx_no = cursor.lastrowid

    #it is necessary to commit your changes using the connection's commit() method.
    cnx.commit()

cursor.close()
cnx.close()