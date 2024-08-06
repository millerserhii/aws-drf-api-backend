resource "aws_ecs_cluster" "webapp_cluster" {
  name = var.CLUSTER_NAME
}
