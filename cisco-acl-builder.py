"""
Cisco ACL Builder
Author: Your Name

Description:
A simple Python script that generates a Cisco IOS Extended Access Control List (ACL)
and optionally applies it to an interface.

This script does NOT connect to a Cisco device.
It simply generates the CLI configuration.
"""


import ipaddress


def network_to_wildcard(network):
    """Convert CIDR notation into Cisco wildcard format."""

    if network.lower() == "any":
        return "any"

    net = ipaddress.ip_network(network, strict=False)

    if net.prefixlen == 32:
        return f"host {net.network_address}"

    wildcard = ipaddress.IPv4Address(
        int(ipaddress.IPv4Address("255.255.255.255")) -
        int(net.netmask)
    )

    return f"{net.network_address} {wildcard}"


print("=" * 45)
print("        CISCO IOS ACL BUILDER")
print("=" * 45)

acl_name = input("\nACL Name: ")

action = input("Action (permit/deny): ").lower()

protocol = input("Protocol (tcp/udp/ip/icmp): ").lower()

source = input(
    "Source Network (Example: 10.10.10.0/24 or any): "
)

destination = input(
    "Destination Network (Example: 192.168.100.10/32 or any): "
)

port = ""

if protocol in ["tcp", "udp"]:
    port = input(
        "Destination Port (Example: 443): "
    )

print("\nGenerating configuration...\n")

source_output = network_to_wildcard(source)
destination_output = network_to_wildcard(destination)

print("=" * 45)
print("GENERATED CISCO CONFIGURATION")
print("=" * 45)
print()

print(f"ip access-list extended {acl_name}")

if port:
    print(
        f" {action} {protocol} "
        f"{source_output} "
        f"{destination_output} "
        f"eq {port}"
    )
else:
    print(
        f" {action} {protocol} "
        f"{source_output} "
        f"{destination_output}"
    )

print("exit")
print()

apply = input("Apply ACL to an interface? (y/n): ").lower()

if apply == "y":

    interface = input(
        "Interface (Example: GigabitEthernet1/0/24): "
    )

    direction = input(
        "Direction (in/out): "
    ).lower()

    print()
    print("=" * 45)
    print("INTERFACE CONFIGURATION")
    print("=" * 45)
    print()

    print(f"interface {interface}")
    print(f" ip access-group {acl_name} {direction}")
    print("exit")

print("\nDone!")