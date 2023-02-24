import json

with open("data.json", "r") as read_file:
    data = json.load(read_file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("------------------------------------------------- --------------------  ------   ------")

for x in range(3):
    attributes = data["imdata"][x]["l1PhysIf"]["attributes"]
    dn = attributes.get("dn")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")
    print("{:<71} {:<10} {:<10}".format(dn, speed, mtu))