import ipaddress

def check_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def check_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def detect_ip_type(ip):
    if check_ipv4(ip):
        return 'IPv4'
    elif check_ipv6(ip):
        return 'IPv6'
    else:
        return 'Bad Ip'


def detect_multiple_ip(ips):
    if isinstance(ips, dict):
        ips = ips.values()
    elif not isinstance(ips, list):
        raise ValueError("WARNING => ips must be a list or dictionary of strings")

    if not all(isinstance(ip, str) for ip in ips):
        raise ValueError("WARNING => ips must contains only strings")

    for ip in ips:
        print(f"{ip} : " + detect_ip_type(ip))
