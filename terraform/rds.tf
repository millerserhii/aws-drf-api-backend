# resource "aws_db_instance" "webapp_postgres_db" {
#     auto_minor_version_upgrade = true
#     storage_type = "standard"
#     engine = "postgres"
#     engine_version = "12"
#     instance_class = "db.t2.micro"
#     username = "postgres"
#     password = "postgres"
#     skip_final_snapshot = true
#     allocated_storage = 20
# }