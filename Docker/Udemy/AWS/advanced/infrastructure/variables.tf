# Variables
variable "aws_region" {
  description = "AWS region for the resources"
  default     = "us-east-1"
}

variable "aws_profile" {
  description = "AWS CLI profile name for authentication"
  default     = "default"
}

variable "terraform_state_bucket" {
  description = "Name of the S3 bucket for Terraform state"
}

variable "terraform_lock_table" {
  description = "Name of the DynamoDB table for state locking"
  default     = "terraform-state-lock"
}

variable "environment" {
  description = "Deployment environment (e.g., dev, prod)"
}

variable "project_name" {
  description = "Name of the project"
}
