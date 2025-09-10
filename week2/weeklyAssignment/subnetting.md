
<!-- Address Block: 192.168.0.0/16 Subnetting need to be implemented for assigning network to 5 different projects
-->


Given Network: 192.168.0.0/16
Total IPs Available: 2^16= 65,536 IP

We need at least 5 subnets. To achieve this, we will borrow 3 bits from the host.

Original subnet mask: 255.255.0.0 (/16)
Borrowing 3 bits from the host portion:
New subnet mask: /19 (255.255.224.0)

Each subnet will have 8,192 IPs

With a /19 subnet mask, the subnet increments by 32 in the third octet (since 256 - 224 = 32).

Subnet mask used: /19 (255.255.224.0)
Total subnets created: 8 (we only use 5 for now)
Each subnet can support 8,190 usable hosts