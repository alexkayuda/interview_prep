# Backend configuration for storing Terraform state
terraform {
  backend "s3" {
    bucket  = var.terraform_state_bucket # Variable for S3 bucket name
    key     = "terraform/state/${var.environment}/ecs_ecr_s3.tfstate"
    region  = var.aws_region
    encrypt = true
  }
}
