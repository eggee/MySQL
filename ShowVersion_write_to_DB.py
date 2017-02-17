import telnetlib
import MySQLdb

#define a list
part_num_list = list()
product_revision_list = list()
result = str()
slot = int()
x = int()
ta5k_ip = '10.13.138.101'
tn = telnetlib.Telnet()

nodes = {
         'Node1': '10.13.138.101',
         'Node6': '10.13.138.106',
         'Node10': '10.13.138.110',
         'Node12': '10.13.138.112',
         'Node15': '10.13.138.115',
         'Node16': '10.13.138.116',
         'Node17': '10.13.138.117',
         'Node18': '10.13.138.118',
         'Node19': '10.13.138.119',
         'Node20': '10.13.138.120',
         'Node21': '10.13.138.121',
         'Node22': '10.13.138.122',
         'Node23': '10.13.138.123',
         'Node24': '10.13.138.124',
         'Node26': '10.13.138.126',
         'Node27': '10.13.138.127',
         'Node28': '10.13.138.128',
         'Node29': '10.13.138.129',
         'Node31': '10.13.138.131',
         'Node32': '10.13.138.132',
         'Node33': '10.13.138.133',
         'Node36': '10.13.138.136',
         'Node37': '10.13.138.137',
         'Node38': '10.13.138.138',
         'Node39': '10.13.138.139'
         }

# nodes = {
#          'Node1': '10.13.138.101',
#          'Node39': '10.13.138.139'
#          }

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
#connect to shelf


def login(ip):
    tn.open(ip)
def login_enable():
    tn.read_until('Username:')
    tn.write('ADMIN\n')
    tn.read_until('Password:')
    tn.write('PASSWORD\n')
    tn.read_until('>')
    tn.write('enable\n')
    tn.read_until('#')
    tn.write('term len 0\n')
    tn.read_until('#')

def show_version(x):
    #tn.write('show version 1/{0} \n'.format(slot))
    tn.write('show version 1/%i \n') %x
    result = tn.read_until('#')
    return result

#MAIN - connect to shelf
for k, v in nodes.items():
    login(v)
    login_enable()
    #call show_version() and save to a variable
    for x in (1,2,3,4,5,6,7,8,9,10,11,'S','A','B',13,14,15,16,17,18,19,20,21,22):
        tn.write('show version 1/{0} \n'.format(x))
        show_version = tn.read_until('#')
        #make a 'string array' or 'list' of the 'show version' output at each of the line-breaks
        #eg a = ['line1', 'line2'], or,
        #eg  a = ['show version\r', '1/1 TA5000 1187550E1 \r', '  Part Number  : 1187550E1\r', ....]
        show_version = show_version.split("\n")
        #display the (long) string-array (i.e. 'list')
        #print show_version
        for line in show_version:
            #if 'print line', then output should be that of original 'show version'
            #print line
            #Find each line with the keyword 'Part Number'
            if 'Part Number' in line:
                #line will look like this - '  Part Number                     : 1187550E1\r'
                #For that line, Make a new 'string array'('list') extracting just the P/N (the 3rd value)
                #from ['Part', 'Number', ':', '1187080L1']
                #part_num_list.append(line.split()[3])
                part_num = (line.split()[3])
        for line in show_version:
            if 'Product Revision' in line:
                #product_revision_list.append(line.split()[3])
                product_revision = (line.split()[3])

        print ("********************************")
        print ("Here is the inventory for {0}, Slot{1}:" .format(k,x))
        print ("Node: {0} , IP: {1} , Slot: {2} , Part_num: {3} , Rev: {4}" .format(k,v,x,part_num,product_revision))
        print ("********************************")

        #insert a record into the database
        sql = """INSERT INTO `BBDLC_INVENTORY`(`NODE_NUM`, `IP`, `SLOT`, `MODULE_NAME`, `PART_NUM`, `REV`)
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""" .format(k,v,x,part_num,part_num,product_revision)
        #Send the SQL statement to the cursor.
        try:
            #execute the SQL command
            cursor.execute(sql)
            #commit changes
            db.commit()
        except:
            # rollback if there is an error
            db.rollback()
            print "Command did not issue correctly"
        else:
            print "SQL command issued without incident"


