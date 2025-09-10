// VPC
resource "aws_vpc" "my-vpc-for-terraform" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "my-vpc-for-terraform"
  }
}

//public-subnet
resource "aws_subnet" "public-subnet" {
  vpc_id     = aws_vpc.my-vpc-for-terraform.id
  cidr_block = "10.0.3.0/24"

  tags = {
    Name = "public-subnet"
  }
}

// internet gateway
resource "aws_internet_gateway" "my-igw" {
  vpc_id = aws_vpc.my-vpc-for-terraform.id

  tags = {
    Name = "my-igw"
  }
}

// public route table
resource "aws_route_table" "my-public-rt" {
  vpc_id = aws_vpc.my-vpc-for-terraform.id

  tags = {
    Name = "my-public-rt"
  }
}

resource "aws_route" "route-to-IGW" {
  route_table_id         = aws_route_table.my-public-rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.my-igw.id
}

resource "aws_route_table_association" "public-subnet-association" {
  subnet_id      = aws_subnet.public-subnet.id
  route_table_id = aws_route_table.my-public-rt.id
}