# -*- coding: utf-8 -*-
import ipaddress

ipaddr = input('IPアドレスを入力してください: ')
netmask = input('プレフィックスを入力してください: ')
cidr = ipaddr + '/' + netmask

print("="*45)
print("")

# ## ネットワークアドレスを取得
nw_address = ipaddress.ip_interface(cidr)
print(f'ネットワークアドレス: {nw_address.network}')

# ## ブロードキャストアドレスを取得
ip_range_addr = ipaddress.ip_network(cidr, strict=False)
print(f'    ブロードキャスト: {ip_range_addr[-1]}')

# ## 使用可能なIPの数
print(f'    使用可能ホスト数: {ip_range_addr.num_addresses-2}')
print(f'      ホストIPの範囲: {ip_range_addr[1]}~{ip_range_addr[-2]}')

# 入力されたIPアドレスのClassを判断する
# Defolt Maskを作成