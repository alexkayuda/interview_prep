# modules/ecs/main.tf
resource "aws_ecs_cluster" "my_ecs" {
  name = var.cluster_name

  setting {
    name  = "containerInsights"
    value = "disabled"
    # value = "enabled"
  }

  tags = var.tags
}
