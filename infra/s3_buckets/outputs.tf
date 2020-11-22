resource "aws_ssm_parameter" "data_store" {
  name  = "/${var.project_name}/data-bucket"
  type  = "String"
  value = aws_s3_bucket.data_store.id
}
