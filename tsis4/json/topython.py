import json
x = open(r'C:\Users\Сырым\Documents\pp2-22B030546\tsis4\json\data.json')
y = json.load(x)
print('''=======================================================================================
DN                                                 Description           Speed    MTU" 
-------------------------------------------------- --------------------  ------  ------''')
sample_data = y["data"]
for i in sample_data:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print("{0:51} {1:20} {2:8} {3:6}".format(dn,descr,speed,mtu))