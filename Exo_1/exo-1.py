import ipaddress

def get_ip():
    ip = input("Entrez une adresse IP (IPv4 ou IPv6) : ")
    return ip

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def is_valid_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def detect_ip_version(ip):
    if is_valid_ipv4(ip):
        return "IPv4"
    elif is_valid_ipv6(ip):
        return "IPv6"
    else:
        return "Adresse invalide"

def validate_ip_list(ip_list):
    result = {}
    for ip in ip_list:
        result[ip] = detect_ip_version(ip)
    return result

def validate_ip_dict(ip_dict):
    result = {}
    for host, ip in ip_dict.items():
        result[host] = detect_ip_version(ip)
    return result

if __name__ == "__main__":
    ip = get_ip()
    print(f"Version de l'adresse : {detect_ip_version(ip)}")

    ip_list = ["192.168.1.1", "2001:db8::ff00:42:8329", "256.256.256.256"]
    print(validate_ip_list(ip_list))

    ip_dict = {"host1": "192.168.1.1", "host2": "2001:db8::ff00:42:8329", "host3": "invalid_ip"}
    print(validate_ip_dict(ip_dict))
