terraform {
  backend "s3" {
    bucket = "my-tfstate-backend-bucket-264"
    region = "ap-south-1"
    key    = "terraform.tfstate"
  }
}


resource "aws_instance" "my-test-ec2" {
  ami           = "ami-0e35ddab05955cf57"
  instance_type = "t2.micro"
  subnet_id     = "subnet-0c72db4847bbb0236"
  tags = {
    "Name" = "my-test-ec2"
  }
}