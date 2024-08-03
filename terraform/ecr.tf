resource "aws_vpc_endpoint" "ecr_api" {
  vpc_id       = data.aws_vpc.default_vpc.id
  service_name = "com.amazonaws.eu-central-1.ecr.api"
  vpc_endpoint_type = "Interface"

  subnet_ids = data.aws_subnets.subnets.ids

  security_group_ids = [
    aws_security_group.ecs_security_group.id
  ]

  private_dns_enabled = true
}

resource "aws_vpc_endpoint" "ecr_dkr" {
  vpc_id       = data.aws_vpc.default_vpc.id
  service_name = "com.amazonaws.eu-central-1.ecr.dkr"
  vpc_endpoint_type = "Interface"

  subnet_ids = data.aws_subnets.subnets.ids

  security_group_ids = [
    aws_security_group.ecs_security_group.id
  ]

  private_dns_enabled = true
}
