#  ip4地址转为int
def ip4_to_int(ip):
    ip_splits = ip.split(".")
    ret = 0
    i = 3
    for ip_split in ip_splits:
        ret = ret | int(ip_split) << i * 8
        i -= 1
    return ret

# int转为ipv4地址
def int_to_ip4(num):
    ips = []
    i = 3
    while i >= 0:
        ip_part = num & 255 << i * 8
        ips.append(str(ip_part >> i*8))
        i -= 1
    return '.'.join(ips)


if __name__ == "__main__":
    ip = "192.168.1.1"
    num = ip4_to_int(ip)
    r_ip = int_to_ip4(num)
    assert(r_ip == ip)