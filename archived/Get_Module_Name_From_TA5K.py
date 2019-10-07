import telnetlib

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
         }

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

def show_version():
    #tn.write('show version 1/{0} \n'.format(slot))
    tn.write('show version 1/1')
    result = tn.read_until('#')
    return result
def show_system():
    #tn.write('show version 1/{0} \n'.format(slot))
    tn.write('show system\n')
    result = tn.read_until('#')
    return result

#MAIN - connect to shelf
for k, v in nodes.items():
    login(v)
    login_enable()
    system = show_system()
    print system
    system = system.split("\n")
    #for each slot, get the module name
    for x in (1,2,3,4,5,6,7,8,9,10,11,'S','A','B',13,14,15,16,17,18,19,20,21,22):
        for line in system:
            #if 'print line', then output should be that of original 'show version'
            #print line
            #Find each line with the keyword 'Part Number'
            # if ('1/{0}' .format %x)  in line:
            if "1/1" in line:
                #line will look like this - '  Part Number                     : 1187550E1\r'
                #For that line, Make a new 'string array'('list') extracting just the P/N (the 3rd value)
                #from ['Part', 'Number', ':', '1187080L1']
                #part_num_list.append(line.split()[3])
                module_name = (line.split()[1])
                print module_name