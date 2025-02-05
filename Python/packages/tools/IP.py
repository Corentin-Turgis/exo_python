import ipaddress
from click import prompt

class IP:
    ip = ''

    def ask_ip(self):
        self.ip = prompt('Entrez une Ip :', '')

    def check_ipv4(self):
        try:
            ipaddress.IPv4Address(self.ip)
            return True
        except ipaddress.AddressValueError:
            return False
