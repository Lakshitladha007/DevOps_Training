resource "aws_instance" "tf-demo-ec2-instance" {
  ami                         = "ami-0e35ddab05955cf57"
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  subnet_id = "subnet-0e68183c5eded2941"
  security_groups = ["${aws_security_group.allow_tls.id}"]
  user_data                   = <<EOF
#!/bin/bash
yes | sudo apt update
yes | sudo apt install apache2
echo "<h1>Server Details</h1><p><strong>Hostname:</strong> $(hostname)</p><p><strong>IP Address:</strong> $(hostname -I | cut -d' ' -f1)</p>" > /var/www/html/index.html
sudo systemctl restart apache2
  EOF
  tags = {
    Name = "tf-test-instance"
  }

}

resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = "vpc-0374778fee2c52b4c"

  tags = {
    Name = "allow_tls"
  }

  dynamic "ingress" {
    for_each = [22, 80, 443, 3306]
    iterator = port
    content {
      description = "TLS from vpc"
      cidr_blocks = ["0.0.0.0/0"]
      protocol    = "tcp"
      from_port   = port.value
      to_port     = port.value
    }
  }
  egress {
    from_port=0
    to_port=0
    protocol=-1
    cidr_blocks=["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}