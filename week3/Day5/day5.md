<!-- 
Launch an ALB in AP-South-1 region and load balance the traffic to 2 EC2 instances.
 -->

Steps:

1. Go to AWS Management Console, search for VPC and create a VPC. Select a CIDR range for you VPC, I selected 12.0.0.0/16

2. Search for Internet Gateway, create a IGW and attach it to the VPC that we created in previous step.

3. Create 2 public subnets and choose the same VPC for both subnets that we created in step1. Also, make the subnets available in 2 different zones, I selected:
   ap-south-1a
   ap-south-2b
The CIDR I selected for both subnets were:
   12.0.1.0/24
   12.0.3.0/24

4. Create a route table in the same VPC, and associate both the subnets to this route table. 
Now, create a route such that the subnets have access to internet.

5. Now, create 2 EC2 instances, one-one in both the subnets.
The important part is the netwrok setting in each EC2 instance:<br>
   Choose the VPC we created.<br>
   For one instance choose one subnet and for other instance choose the left subnet.<br>
   Enable assigning public IP for both the instances.<br>
   Create a security group, such that apart from SSH we can also make HTTP request as we are going to install apache on these EC2 instances.<br>
   In userdata section, write the script to Bootstrap the EC2 instacne.<br>

``` Bash

#!/bin/bash
yes | sudo apt update

yes | sudo apt install apache2

echo "<h1>Server Details</h1>
<p><strong>Hostname:</strong> $(hostname)</p>
<p><strong>IP Address:</strong> $(hostname -I | cut -d' ' -f1)</p>" | sudo tee /var/www/html/index.html

sudo systemctl restart apache2

```
and finaly Launch instance.

6. Verify whether apache has been installed on our EC2 instance or not, by using the public IP of EC2 instance and run it in chrome.

7. Create a target group and club both EC2 instances in that, select the VPC that we created.

8. Final step is to create a Application Load Balancer and make it internet facing.
Create a security group for allowing access from internet. And finally click on create LB.
Copy the DNS name of load balancer and run on chrome to verify whether requests are forwarded to different servers or not.

LoadBalancer Screenshot:
![LoadBalancer Screenshot](Screenshots/loadBalancer.png)

TargetGroup Screenshot:
![TargetGroup Screenshot](Screenshots/targetGroup.png)

Ec2 Instance1 Screenshot:
![Ec2 Instance1 Screenshot](Screenshots/ec2Instance1.png)
 
Ec2 Instance2 Screenshot:
![Ec2 Instance2 Screenshot](Screenshots/ec2Instance2.png)

Output on Instance1 Screenshot:
![Output on Instance1 Screenshot](Screenshots/outputOnInstance1.png)

Output on Instance2 Screenshot:
![Output on Instance2 Screenshot](Screenshots/outputOnInstance2.png)
