<!-- 
Subnet the Class C IP Address 205.11.2.0 so that you have 30 subnets. What is the subnet mask for the maximum number of hosts? How many hosts can each subnet have? What is the IP address of host 3 on subnet 2? 
 -->

The IP Address belongs to Class C, so only 8 Host bits are available.

Since, we need 30 subnets, so need to borrow 5 host bits. As: 2^5=32, which is greater than 30.

A Class C IP address has a default subnet mask of 255.255.255.0.

1. Since, 5 bits are borrowed, 3 bits are still left from the octet. Converting the last octet to decimal: 11100000=224
Therefore, the subnet mask is 255.255.255.224.

2. Total hosts per subnet is: 
          => 2^h-2 ; where 'h' is no. of host bits.
          => 2^3-2
          => 6

3. Subnet 0: 205.11.2.0
Subnet 1: 205.11.2.32
Subnet 2: 205.11.2.64, and so on.

Therefore:
Subnet mask: 255.255.255.224
Hosts per subnet: 6
IP address of host 3 on subnet 2: 205.11.2.67
