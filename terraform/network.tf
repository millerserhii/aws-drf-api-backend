# TODO: configure the VPC and subnet for the app

# resource "aws_vpc" "webapp_vpc" {
#   cidr_block = "10.0.0.0/16"
#   enable_dns_support   = true
#   enable_dns_hostnames = true

#   tags = {
#     Name = "webapp_vpc"
#   }
# }

# resource "aws_subnet" "webapp_subnet" {
#   vpc_id     = aws_vpc.webapp_vpc.id
#   cidr_block = "10.0.1.0/24"

#   tags = {
#     Name = "webapp_subnet"
#   }
# }

data "aws_vpc" "default_vpc" {
  default = true
}

data "aws_subnets" "subnets" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default_vpc.id]
  }
}
