terraform {
  backend "s3" {
    bucket         = "mserh-terraform-state"
    key            = "pure-ts-webapp/terraform.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "terraform-state-locking"
    encrypt        = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.26"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}
