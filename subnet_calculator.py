# Subnet calculator

import ipaddress

ip_address = input("Enter an IP address: ")
subnet_mask = int(input("Enter the subnet mask in CIDR notation: /"))

joined = f"{ip_address}/{subnet_mask}"
network_id = ipaddress.ip_network(joined, strict=False)

print(f"Network ID: {network_id}\nNetmask: {network_id.netmask}\nBroadcast Address: {network_id.broadcast_address}\nTotal valid hosts: {network_id.num_addresses - 2}")
print(f"Usable Host Range: {network_id[1]} - {network_id[-2]}")