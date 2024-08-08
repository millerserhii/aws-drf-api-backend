# TODO: configure the VPC and subnet for the app

data "aws_vpc" "default_vpc" {
  default = true
}

data "aws_subnets" "subnets" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default_vpc.id]
  }
}

# Interface Endpoint for ECR API
resource "aws_vpc_endpoint" "ecr_api" {
  vpc_id            = data.aws_vpc.default_vpc.id
  service_name      = "com.amazonaws.${data.aws_region.current.name}.ecr.api"
  vpc_endpoint_type = "Interface"

  subnet_ids         = data.aws_subnets.subnets.ids
  security_group_ids = [aws_security_group.ecr_endpoint_sg.id]
}

# Interface Endpoint for ECR DKR
resource "aws_vpc_endpoint" "ecr_dkr" {
  vpc_id            = data.aws_vpc.default_vpc.id
  service_name      = "com.amazonaws.${data.aws_region.current.name}.ecr.dkr"
  vpc_endpoint_type = "Interface"

  subnet_ids         = data.aws_subnets.subnets.ids
  security_group_ids = [aws_security_group.ecr_endpoint_sg.id]
}

# Gateway Endpoint for S3
resource "aws_vpc_endpoint" "s3" {
  vpc_id       = data.aws_vpc.default_vpc.id
  service_name = "com.amazonaws.${data.aws_region.current.name}.s3"
  vpc_endpoint_type = "Gateway"

  route_table_ids = data.aws_route_tables.default_route_tables.ids
}

# Fetch Route Tables for the default VPC
data "aws_route_tables" "default_route_tables" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default_vpc.id]
  }
}
