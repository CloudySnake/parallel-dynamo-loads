resource "aws_ssm_parameter" "data_store" {
  name  = "/${var.project_name}/data-bucket"
  type  = "String"
  value = aws_s3_bucket.data_store.id
}

output "s3_bucket_arn" {
  value = aws_s3_bucket.data_store.arn
}
