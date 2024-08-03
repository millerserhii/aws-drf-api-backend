resource "aws_ecs_task_definition" "webapp_task" {
  family                   = "webapp-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.ecs_execution_role.arn

  container_definitions = jsonencode([{
    name  = "webapp-container",
    image = "public.ecr.aws/g9x5w2d4/pure-ts-public:latest"
    portMappings = [{
      containerPort = 8000,
      hostPort      = 8000
    }]
  }])
}

resource "aws_ecs_service" "webapp_service" {
  name            = "webapp-service"
  cluster         = aws_ecs_cluster.webapp_cluster.id
  task_definition = aws_ecs_task_definition.webapp_task.arn
  launch_type     = "FARGATE"

  network_configuration {
    subnets = data.aws_subnets.subnets.ids
    security_groups = [aws_security_group.ecs_security_group.id]
  }
  load_balancer {
    target_group_arn = aws_lb_target_group.ecs-target-group.arn
    container_name   = "webapp-container"
    container_port   = 8000
  }

  desired_count = 1
}
