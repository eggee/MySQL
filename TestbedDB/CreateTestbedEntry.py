from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='bbdlc', password='bbdlc',
                              host='10.21.1.181',
                              database='Inventory')
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_tb_entry = ("INSERT INTO photon_testbeds "
               "(tb_name, device, part_no, serial_no, ip_addr) "
               "VALUES (%s, %s, %s, %s, %s)")
# add_salary = ("INSERT INTO salaries "
#               "(emp_no, salary, from_date, to_date) "
#               "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_tb_entry = ('MCI-1', 'OLT-1', '1187xxxx', 'ADTN12345678', '10.13.245.321')

# Insert new employee
cursor.execute(add_tb_entry, data_tb_entry)
indx_no = cursor.lastrowid

# Insert salary information
# data_salary = {
#   'emp_no': emp_no,
#   'salary': 50000,
#   'from_date': tomorrow,
#   'to_date': date(9999, 1, 1),
# }
# cursor.execute(add_salary, data_salary)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()