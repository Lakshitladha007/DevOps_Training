terraform {
  backend "s3" {
    bucket = "my-remote-backend-s3-264"
    region = "ap-south-1"
    key    = "terraform.tfstate"
  }
}

module "my-ec2-instance" {
  source = "./modules/EC2-instance"
}