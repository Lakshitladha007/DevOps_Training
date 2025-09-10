// while importing a resource body of resource should be empty
resource "aws_instance" "my-test-ec2" {
   ami= "ami-0e35ddab05955cf57"
   instance_type= "t2.micro"
   tags={
    "Name"="my-test-ec2"
   }
}