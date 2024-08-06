variable "RDS_USERNAME" {
  description = "The username for the RDS instance"
  type        = string
}

variable "RDS_PASSWORD" {
  description = "The password for the RDS instance"
  type        = string
  sensitive   = true
}

variable "REDIS_USER" {
  description = "The username for the Redis instance"
  type        = string
}

variable "REDIS_PASSWORD" {
  description = "The password for the Redis instance"
  type        = string
  sensitive   = true
}

variable "APP_CONTAINER_PORT" {
  description = "The port on which the app container listens"
  type        = number
  default     = 8000
}

variable "APP_HOST_PORT" {
  description = "The port on which the app host listens"
  type        = number
  default     = 8000
}

variable "ECR_REPOSITORY" {
  description = "The Docker image to use for the app container"
  type        = string
  default     = "aws-drf-boilerplate"
}

variable "CONTAINER_NAME" {
  description = "The name of the container"
  type        = string
  default     = "webapp-container"
}

variable "SERVICE_NAME" {
  description = "The name of the ECS service"
  type        = string
  default     = "webapp-service"
}

variable "CLUSTER_NAME" {
  description = "The name of the ECS cluster"
  type        = string
  default     = "webapp-ecs-cluster"
}

variable "TASK_FAMILY" {
  description = "The family name of the ECS task"
  type        = string
  default     = "webapp-task"
}
