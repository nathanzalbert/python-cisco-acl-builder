# Cisco ACL Builder

A Python tool that generates Cisco IOS Extended Access Control List (ACL) configurations from user input. The script simplifies ACL creation by converting network information into valid Cisco CLI commands.

## Features

* Generate Cisco IOS Extended ACLs
* Supports TCP, UDP, ICMP, and IP
* Converts CIDR notation to Cisco wildcard masks
* Optionally generates interface ACL application commands

## Requirements

* Python 3.x

## Usage

```bash
python cisco_acl_builder.py
```

Follow the prompts to generate your Cisco ACL configuration.

## Example Output

```cisco
ip access-list extended WEB-ACL
 permit tcp 10.10.10.0 0.0.0.255 host 192.168.100.10 eq 443
exit

interface GigabitEthernet1/0/24
 ip access-group WEB-ACL in
exit
```

## Skills Demonstrated

* Python
* Cisco IOS
* Network Security
* Access Control Lists (ACLs)
* Network Automation
