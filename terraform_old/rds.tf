resource "aws_db_instance" "webapp_postgres_db" {
  auto_minor_version_upgrade = true
  storage_type               = "standard"
  engine                     = "postgres"
  engine_version             = "14"
  instance_class             = "db.t3.micro"
  publicly_accessible        = true
  username                   = var.RDS_USERNAME
  password                   = var.RDS_PASSWORD
  skip_final_snapshot        = true
  allocated_storage          = 20

  vpc_security_group_ids     = [aws_security_group.webapp_db_sg.id]
}

resource "aws_security_group" "webapp_db_sg" {
  name        = "webapp-db-sg"
  description = "Security group for RDS instance"
  vpc_id      = data.aws_vpc.default_vpc.id

  ingress {
    description = "PostgreSQL"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allowing inbound traffic from all IPs. Adjust for better security.
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # All traffic
    cidr_blocks = ["0.0.0.0/0"]
  }
}
