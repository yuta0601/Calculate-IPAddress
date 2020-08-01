ip_str = '192.168.1.1'
ip_list = list(map(int, ip_str.split('.')))
ip_list

# [192, 168, 1, 1]

nw_address = ipaddress.ip_interface(cidr)
print(f'ネットワークアドレス: {nw_address.network}')
# print(type(nw_address.network))
# <class 'ipaddress.IPv4Network'>



ip_range_addr = ipaddress.ip_network(cidr, strict=False)
print(f'    ブロードキャスト: {ip_range_addr[-1]}')
# print(type(ip_range_addr[-1]))
# <class 'ipaddress.IPv4Address'>



print(f'    使用可能ホスト数: {ip_range_addr.num_addresses-2}')
# print(type(ip_range_addr.num_addresses))
# <class 'int'>
print(f'      ホストIPの範囲: {ip_range_addr[1]}~{ip_range_addr[-2]}')