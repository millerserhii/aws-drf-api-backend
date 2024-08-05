variable "db_username" {
  description = "The username for the RDS instance"
  type        = string
}

variable "db_password" {
  description = "The password for the RDS instance"
  type        = string
  sensitive   = true
}

variable "AWS_DEFAULT_REGION" {
  description = "The AWS region to deploy to"
  type        = string
  default     = "eu-central-1"
}


variable "AWS_ACCESS_KEY_ID" {
  description = "The AWS access key ID"
  type        = string
}

variable "AWS_SECRET_ACCESS_KEY" {
  description = "The AWS access key ID"
  type        = string
}
