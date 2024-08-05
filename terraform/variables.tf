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
