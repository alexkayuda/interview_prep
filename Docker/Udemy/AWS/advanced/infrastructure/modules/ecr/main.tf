# modules/ecr/main.tf
resource "aws_ecr_repository" "my_ecr" {
  name                 = var.repository_name
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }

  tags = var.tags
}
