# Root Terraform configuration to manage AWS resources using modules and environments


# Provider configuration
provider "aws" {
  region = var.aws_region
  # profile = var.aws_profile # Optional: Supports multiple profiles
}

# Backend configuration for storing Terraform state
terraform {
  required_version = ">= 1.10.2"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  backend "s3" {
    bucket         = var.terraform_state_bucket
    key            = "terraform/state/${var.environment}/ecs_ecr_s3.tfstate"
    region         = var.aws_region
    encrypt        = true
    dynamodb_table = var.terraform_lock_table # Locking table for state management
  }
}

# Call the S3 module
module "s3" {
  source = "./modules/s3"

  bucket_name = var.terraform_state_bucket
  tags = {
    Environment = var.environment
    Project     = var.project_name
  }
}

# Call the ECR module
module "ecr" {
  source = "./modules/ecr"

  repository_name = "${var.project_name}-${var.environment}-ecr-repository"
  tags = {
    Environment = var.environment
    Project     = var.project_name
  }
}

# Call the ECS module
module "ecs" {
  source = "./modules/ecs"

  cluster_name = "${var.project_name}-${var.environment}-ecs-cluster"
  tags = {
    Environment = var.environment
    Project     = var.project_name
  }
}
