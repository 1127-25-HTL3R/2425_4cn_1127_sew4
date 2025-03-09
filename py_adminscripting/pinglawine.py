
__author__ = "Felix Friesenbichler"
__email__ = "1127@htl.rennweg.at"
__license__ = "GPLv2"

import ipaddress
import subprocess

def ping_subnet(network_address: str) -> None:
    try:
        network: ipaddress.IPv4Network = ipaddress.ip_network(network_address, strict=False)
        for host in network.hosts():
            print(f'Pinge {host}...')
            subprocess.run(['ping', '-n', '4', str(host)], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except ValueError as e:
        print(f'Ungültige Netzwerkadresse: {e}')

if __name__ == "__main__":
    ip_input: str = input("Bitte geben Sie eine IP-Adresse mit Netzwerk-Suffix ein (z.B. 192.168.1.0/24): ")
    ping_subnet(ip_input)
