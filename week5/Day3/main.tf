resource "aws_instance" "my-test-ec2" {
  ami                         = "ami-0e35ddab05955cf57"
  instance_type               = "t2.micro"
  associate_public_ip_address = true
  subnet_id                   = "subnet-02df917eb0c15c22d"
  security_groups             = ["${aws_security_group.allow_tls.id}"]
  key_name                    = aws_key_pair.name.key_name
  tags = {
    "Name" = "my-test-ec2"
  }
}

resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = "vpc-0c024c72e3add17db"

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
    from_port        = 0
    to_port          = 0
    protocol         = -1
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

resource "aws_key_pair" "name" {
  key_name   = "my-key-for-ec2"
  public_key = file("${path.module}/my-test-key-pair.pub")
}