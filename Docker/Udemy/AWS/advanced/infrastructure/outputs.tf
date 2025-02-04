# Outputs
output "s3_bucket_name" {
  value = module.s3.bucket_name
}

output "ecr_repository_url" {
  value = module.ecr.repository_url
}

output "ecs_cluster_name" {
  value = module.ecs.cluster_name
}
