import MySQLdb

#connect and login to an existing server (ip, username, password, Database)
#db = MySQLdb.connect("10.21.1.181","bbdlc","bbdlc","bbdlc")
db = MySQLdb.connect("10.21.1.181","bbdlc","bbdlc","Inventory")
# prepare a cursor object using cursor() method
cursor = db.cursor()
#check the version to very connectivity
cursor.execute("SELECT VERSION()")
#'fetch' the line that was output
data = cursor.fetchone()
#display it
print "Database version : %s " %data

#insert a record into the database
#sql = """INSERT INTO `TEST-TABLE`(`FIRST_NAME`, `LAST_NAME`, `AGE`, `SEX`, `INCOME`) VALUES ('JANE', 'DOE', '45', 'F', '8000')"""

# Create a new table on the given Database
sql = """CREATE TABLE BBDLC_INVENTORY (
         NODE_NUM CHAR(20) NOT NULL,
         IP CHAR(20),
         SLOT_NUM INT,
         MODULE_NAME CHAR(20),
         PART_NUM CHAR(20),
         REV CHAR(4) )"""

#Send the SQL statement to the cursor.
try:
    #execute the SQL command
    cursor.execute(sql)
    #commit changes
    db.commit()
except:
    # rollback if there is an error
    db.rollback()
else:
    print "SQL command issued without incident"

db.close()