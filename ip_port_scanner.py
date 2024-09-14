import socket
import ssl
import os
import platform
from pystyle import Colorate, Colors

def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def get_ip_and_port(site):
    try:
        ip_address = socket.gethostbyname(site)
        print(Colorate.Horizontal(Colors.purple_to_red, f"The IP address of {site} is {ip_address}"))

        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=site) as s:
            s.connect((site, 443))
            print(Colorate.Horizontal(Colors.purple_to_red, f"{site} uses HTTPS on port 443"))
            return ip_address, 443
    except ssl.SSLError:
        print(Colorate.Horizontal(Colors.purple_to_red, f"{site} uses HTTP on port 80"))
        return ip_address, 80
    except socket.gaierror:
        return None, None
    except Exception as e:
        print(Colorate.Horizontal(Colors.purple_to_red, f"Error during verification: {e}"))
        return None, None

def display_ascii_art():
    ascii_art = """
    ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
    ██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    ██║██████╔╝       ██║   ██║   ██║██║   ██║██║     
    ██║██╔═══╝        ██║   ██║   ██║██║   ██║██║     
    ██║██║            ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚═╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                    By dataexe
    """
    print(Colorate.Horizontal(Colors.purple_to_red, ascii_art))

def display_menu():
    menu = """
    ╔════════════════════════════════╗
       Discord: dataexe
       GitHub: github.com/dataexepy
    ╚════════════════════════════════╝
    
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      [1] Test a website
      [2] Scan common ports
      [3] Perform DNS lookup
      [0] EXIT
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    print(Colorate.Horizontal(Colors.purple_to_red, menu))

def scan_common_ports(ip):
    common_ports = [21, 22, 80, 443, 3306, 8080]
    open_ports = []
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def perform_dns_lookup(domain):
    try:
        return socket.gethostbyname_ex(domain)
    except socket.gaierror:
        return None

def main():
    while True:
        clear_screen()
        display_ascii_art()
        display_menu()
        choice = input(Colorate.Horizontal(Colors.purple_to_red, "\nSelect an option: "))

        if choice == "1":
            site = input(Colorate.Horizontal(Colors.purple_to_red, "Enter the website name (e.g., www.example.com): "))
            ip_address, port = get_ip_and_port(site)
            if ip_address is None:
                print(Colorate.Horizontal(Colors.red_to_purple, "Error: Invalid or unfound domain name."))
        elif choice == "2":
            ip = input(Colorate.Horizontal(Colors.purple_to_red, "Enter the IP address to scan: "))
            open_ports = scan_common_ports(ip)
            if open_ports:
                print(Colorate.Horizontal(Colors.purple_to_red, f"Open ports: {', '.join(map(str, open_ports))}"))
            else:
                print(Colorate.Horizontal(Colors.purple_to_red, "No common ports are open."))
        elif choice == "3":
            domain = input(Colorate.Horizontal(Colors.purple_to_red, "Enter the domain name for DNS lookup: "))
            result = perform_dns_lookup(domain)
            if result:
                hostname, aliases, ips = result
                print(Colorate.Horizontal(Colors.purple_to_red, f"Hostname: {hostname}"))
                print(Colorate.Horizontal(Colors.purple_to_red, f"Aliases: {', '.join(aliases)}"))
                print(Colorate.Horizontal(Colors.purple_to_red, f"IP Addresses: {', '.join(ips)}"))
            else:
                print(Colorate.Horizontal(Colors.red_to_purple, "DNS lookup failed."))
        elif choice == "0":
            print(Colorate.Horizontal(Colors.red_to_purple, "Goodbye!"))
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_purple, "Invalid option."))
        
        input(Colorate.Horizontal(Colors.red_to_purple, "Press Enter to continue..."))

if __name__ == "__main__":
    main()
